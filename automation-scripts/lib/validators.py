import subprocess
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class ValidationError:
    file: str
    line: Optional[int]
    message: str
    parser: str


@dataclass
class ValidationResult:
    file: str
    valid: bool
    errors: List[ValidationError]
    parser_used: Optional[str] = None


def validate_sql_syntax(file_path: Path, try_mysql: bool = True, try_postgres: bool = True) -> ValidationResult:
    """
    Validate SQL file syntax using MySQL and/or PostgreSQL parsers.
    Tries MySQL first, falls back to PostgreSQL if MySQL fails and try_postgres=True.
    
    Args:
        file_path: Path to SQL file
        try_mysql: Whether to try MySQL parser
        try_postgres: Whether to try PostgreSQL parser
    
    Returns:
        ValidationResult with syntax check results
    """
    errors = []
    
    if try_mysql:
        result = _validate_mysql(file_path)
        if result.valid:
            return result
        errors.extend(result.errors)
    
    if try_postgres:
        result = _validate_postgres(file_path)
        if result.valid:
            return result
        errors.extend(result.errors)
    
    return ValidationResult(
        file=str(file_path),
        valid=False,
        errors=errors,
        parser_used=None
    )


def _validate_mysql(file_path: Path) -> ValidationResult:
    """Validate SQL syntax using MySQL parser."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        result = subprocess.run(
            ['mysql', '--batch', '--skip-column-names', '-e', f'delimiter //\n{sql_content}\n//'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            return ValidationResult(
                file=str(file_path),
                valid=True,
                errors=[],
                parser_used='mysql'
            )
        
        errors = _parse_mysql_errors(str(file_path), result.stderr)
        return ValidationResult(
            file=str(file_path),
            valid=False,
            errors=errors,
            parser_used='mysql'
        )
    
    except subprocess.TimeoutExpired:
        return ValidationResult(
            file=str(file_path),
            valid=False,
            errors=[ValidationError(
                file=str(file_path),
                line=None,
                message="Validation timeout (>10s)",
                parser='mysql'
            )],
            parser_used='mysql'
        )
    except FileNotFoundError:
        return ValidationResult(
            file=str(file_path),
            valid=False,
            errors=[ValidationError(
                file=str(file_path),
                line=None,
                message="MySQL client not found",
                parser='mysql'
            )],
            parser_used='mysql'
        )
    except Exception as e:
        return ValidationResult(
            file=str(file_path),
            valid=False,
            errors=[ValidationError(
                file=str(file_path),
                line=None,
                message=f"Unexpected error: {str(e)}",
                parser='mysql'
            )],
            parser_used='mysql'
        )


def _validate_postgres(file_path: Path) -> ValidationResult:
    """Validate SQL syntax using PostgreSQL parser."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        result = subprocess.run(
            ['psql', '--no-psqlrc', '--set', 'ON_ERROR_STOP=1', '-c', sql_content],
            capture_output=True,
            text=True,
            timeout=10,
            env={'PGHOST': 'localhost', 'PGDATABASE': 'postgres'}
        )
        
        if result.returncode == 0 or 'FATAL' not in result.stderr:
            return ValidationResult(
                file=str(file_path),
                valid=True,
                errors=[],
                parser_used='postgresql'
            )
        
        errors = _parse_postgres_errors(str(file_path), result.stderr)
        return ValidationResult(
            file=str(file_path),
            valid=False,
            errors=errors,
            parser_used='postgresql'
        )
    
    except subprocess.TimeoutExpired:
        return ValidationResult(
            file=str(file_path),
            valid=False,
            errors=[ValidationError(
                file=str(file_path),
                line=None,
                message="Validation timeout (>10s)",
                parser='postgresql'
            )],
            parser_used='postgresql'
        )
    except FileNotFoundError:
        return ValidationResult(
            file=str(file_path),
            valid=False,
            errors=[ValidationError(
                file=str(file_path),
                line=None,
                message="PostgreSQL client not found",
                parser='postgresql'
            )],
            parser_used='postgresql'
        )
    except Exception as e:
        return ValidationResult(
            file=str(file_path),
            valid=False,
            errors=[ValidationError(
                file=str(file_path),
                line=None,
                message=f"Unexpected error: {str(e)}",
                parser='postgresql'
            )],
            parser_used='postgresql'
        )


def _parse_mysql_errors(file_path: str, stderr: str) -> List[ValidationError]:
    """Parse MySQL error messages into structured format."""
    errors = []
    
    error_pattern = re.compile(r'ERROR\s+\d+\s+\([\w\d]+\)\s+at\s+line\s+(\d+):\s+(.+)')
    for match in error_pattern.finditer(stderr):
        line_num = int(match.group(1))
        message = match.group(2).strip()
        errors.append(ValidationError(
            file=file_path,
            line=line_num,
            message=message,
            parser='mysql'
        ))
    
    if not errors and stderr.strip():
        general_error_pattern = re.compile(r'ERROR\s+\d+\s+\([\w\d]+\):\s+(.+)')
        match = general_error_pattern.search(stderr)
        if match:
            errors.append(ValidationError(
                file=file_path,
                line=None,
                message=match.group(1).strip(),
                parser='mysql'
            ))
        else:
            errors.append(ValidationError(
                file=file_path,
                line=None,
                message=stderr.strip()[:200],
                parser='mysql'
            ))
    
    return errors


def _parse_postgres_errors(file_path: str, stderr: str) -> List[ValidationError]:
    """Parse PostgreSQL error messages into structured format."""
    errors = []
    
    error_pattern = re.compile(r'ERROR:\s+(.+?)(?:\nLINE\s+(\d+):)?', re.MULTILINE)
    for match in error_pattern.finditer(stderr):
        message = match.group(1).strip()
        line_num = int(match.group(2)) if match.group(2) else None
        errors.append(ValidationError(
            file=file_path,
            line=line_num,
            message=message,
            parser='postgresql'
        ))
    
    if not errors and stderr.strip() and 'FATAL' not in stderr:
        errors.append(ValidationError(
            file=file_path,
            line=None,
            message=stderr.strip()[:200],
            parser='postgresql'
        ))
    
    return errors


def validate_basic_sql(file_path: Path) -> ValidationResult:
    """
    Minimal validation for Lab 7 or creative labs.
    Only checks if file exists and can be read.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.strip():
            return ValidationResult(
                file=str(file_path),
                valid=False,
                errors=[ValidationError(
                    file=str(file_path),
                    line=None,
                    message="File is empty",
                    parser='basic'
                )],
                parser_used='basic'
            )
        
        basic_checks = [
            (r'\bSELECT\b|\bINSERT\b|\bUPDATE\b|\bDELETE\b|\bCREATE\b|\bDROP\b|\bALTER\b',
             "No SQL keywords found"),
        ]
        
        for pattern, error_msg in basic_checks:
            if not re.search(pattern, content, re.IGNORECASE):
                return ValidationResult(
                    file=str(file_path),
                    valid=False,
                    errors=[ValidationError(
                        file=str(file_path),
                        line=None,
                        message=error_msg,
                        parser='basic'
                    )],
                    parser_used='basic'
                )
        
        return ValidationResult(
            file=str(file_path),
            valid=True,
            errors=[],
            parser_used='basic'
        )
    
    except Exception as e:
        return ValidationResult(
            file=str(file_path),
            valid=False,
            errors=[ValidationError(
                file=str(file_path),
                line=None,
                message=f"Cannot read file: {str(e)}",
                parser='basic'
            )],
            parser_used='basic'
        )
