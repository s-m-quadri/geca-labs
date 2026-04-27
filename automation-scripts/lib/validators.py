import os
import re
import shlex
import subprocess
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional, Tuple

from lib.writeup.source import strip_sql_comments


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
    Validate SQL syntax without requiring databases or tables.

    Prefer **sqlglot** parse-only checks (matches MySQL then PostgreSQL dialects). That avoids false
    failures when scripts contain ``USE db`` / queries against tables created in other files.

    If sqlglot is not installed, falls back to ``mysql`` / ``psql`` subprocess validation (needs live servers).
    """
    fp = str(file_path)
    try:
        content = Path(file_path).read_text(encoding="utf-8")
    except OSError as e:
        return ValidationResult(
            file=fp,
            valid=False,
            errors=[
                ValidationError(file=fp, line=None, message=str(e), parser="read"),
            ],
            parser_used=None,
        )

    # Comment-only files: nothing executable to validate
    if not strip_sql_comments(content).strip():
        return ValidationResult(file=fp, valid=True, errors=[], parser_used="mysql")

    parsed = _validate_sqlglot_only(fp, content, try_mysql=try_mysql, try_postgres=try_postgres)
    if parsed is not None:
        return parsed

    errors: List[ValidationError] = []

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
        file=fp,
        valid=False,
        errors=errors,
        parser_used=None,
    )


def _validate_sqlglot_only(
    fp: str,
    content: str,
    *,
    try_mysql: bool,
    try_postgres: bool,
) -> Optional[ValidationResult]:
    """Parse-only validation; returns None if sqlglot is unavailable."""
    try:
        import sqlglot
        from sqlglot.errors import ParseError
    except ImportError:
        return None

    mysql_fail: Optional[str] = None
    pg_fail: Optional[str] = None

    if try_mysql:
        try:
            sqlglot.parse(content, dialect="mysql")
            return ValidationResult(file=fp, valid=True, errors=[], parser_used="mysql")
        except ParseError as e:
            mysql_fail = str(e).strip()[:800]

    if try_postgres:
        try:
            sqlglot.parse(content, dialect="postgres")
            return ValidationResult(file=fp, valid=True, errors=[], parser_used="postgresql")
        except ParseError as e:
            pg_fail = str(e).strip()[:800]

    errs: List[ValidationError] = []
    if mysql_fail:
        errs.append(
            ValidationError(file=fp, line=None, message=f"MySQL dialect parse: {mysql_fail}", parser="mysql")
        )
    if pg_fail:
        errs.append(
            ValidationError(file=fp, line=None, message=f"PostgreSQL dialect parse: {pg_fail}", parser="postgresql")
        )
    if not errs:
        errs.append(
            ValidationError(file=fp, line=None, message="Could not parse SQL with sqlglot.", parser="sqlglot")
        )
    return ValidationResult(file=fp, valid=False, errors=errs, parser_used=None)


def _mysql_cli_prefix() -> List[str]:
    """Optional extra args, e.g. CI: ``-h127.0.0.1 -ulint -plint`` from ``SQL_VALIDATE_MYSQL_FLAGS``."""
    flags = os.environ.get("SQL_VALIDATE_MYSQL_FLAGS", "").strip()
    return shlex.split(flags) if flags else []


def _validate_mysql(file_path: Path) -> ValidationResult:
    """Validate SQL syntax using MySQL parser."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            sql_content = f.read()

        cmd = [
            "mysql",
            *_mysql_cli_prefix(),
            "--batch",
            "--skip-column-names",
            "-e",
            f"delimiter //\n{sql_content}\n//",
        ]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=10,
        )
        
        if result.returncode == 0:
            return ValidationResult(
                file=str(file_path),
                valid=True,
                errors=[],
                parser_used='mysql'
            )

        errors = _parse_mysql_errors(str(file_path), result.stderr + "\n" + result.stdout)
        if not errors:
            msg = (result.stderr or result.stdout or "").strip() or f"mysql exited with code {result.returncode}"
            errors = [
                ValidationError(
                    file=str(file_path),
                    line=None,
                    message=msg[:500],
                    parser='mysql',
                )
            ]
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
        
        # Inherit PATH and PG* from the environment (CI sets PGHOST/PGUSER/PGPASSWORD/PGDATABASE via GITHUB_ENV).
        env = {**os.environ}
        result = subprocess.run(
            ["psql", "--no-psqlrc", "--set", "ON_ERROR_STOP=1", "-c", sql_content],
            capture_output=True,
            text=True,
            timeout=10,
            env=env,
        )

        # Only a zero exit code means success. The old `or 'FATAL' not in stderr`
        # treated connection failures and syntax errors as OK when MySQL had already failed.
        if result.returncode == 0:
            return ValidationResult(
                file=str(file_path),
                valid=True,
                errors=[],
                parser_used='postgresql'
            )

        errors = _parse_postgres_errors(str(file_path), result.stderr + "\n" + result.stdout)
        if not errors:
            msg = (result.stderr or result.stdout or "").strip() or f"psql exited with code {result.returncode}"
            errors = [
                ValidationError(
                    file=str(file_path),
                    line=None,
                    message=msg[:500],
                    parser='postgresql',
                )
            ]
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
