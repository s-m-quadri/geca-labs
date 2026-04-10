#!/usr/bin/env python3

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple, Dict
from dataclasses import dataclass

from lib.validators import validate_sql_syntax, validate_basic_sql, ValidationResult


@dataclass
class TestConfig:
    lab_number: str
    lab_branch: str
    completion_threshold: float = 0.75
    is_lab_07: bool = False


@dataclass
class TestReport:
    total_files: int
    modified_files: int
    completion_ratio: float
    validation_results: List[ValidationResult]
    passed: bool
    errors_count: int


def parse_arguments():
    parser = argparse.ArgumentParser(description='Test DBMS lab submission')
    parser.add_argument('--lab-branch', required=True, help='Lab branch name (e.g., lab-dbms-04)')
    parser.add_argument('--threshold', type=float, default=0.75, help='Completion threshold (default: 0.75)')
    return parser.parse_args()


def get_lab_config(lab_branch: str, threshold: float) -> TestConfig:
    """Extract lab configuration from branch name."""
    lab_num = lab_branch.split('-')[-1] if '-' in lab_branch else '00'
    is_lab_07 = lab_num == '07'
    
    return TestConfig(
        lab_number=lab_num,
        lab_branch=lab_branch,
        completion_threshold=threshold,
        is_lab_07=is_lab_07
    )


def fetch_baseline_files(lab_branch: str) -> List[str]:
    """
    Fetch list of SQL task files from the baseline orphan branch.
    Excludes setup and check_status files from task count.
    """
    try:
        result = subprocess.run(
            ['git', 'ls-tree', '-r', '--name-only', f'origin/{lab_branch}'],
            capture_output=True,
            text=True,
            check=True
        )
        
        all_files = [f.strip() for f in result.stdout.strip().split('\n') if f.strip().endswith('.sql')]
        
        task_files = [
            f for f in all_files
            if not f.endswith('_setup.sql') 
            and not f.endswith('check_status.sql')
            and not f.startswith('.')
        ]
        
        return task_files
    
    except subprocess.CalledProcessError as e:
        print(f"Error fetching baseline from {lab_branch}: {e.stderr}", file=sys.stderr)
        return []


def get_modified_files(lab_branch: str) -> List[str]:
    """Get list of modified SQL files compared to baseline."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', f'origin/{lab_branch}', 'HEAD'],
            capture_output=True,
            text=True,
            check=True
        )
        
        modified = [
            f.strip() for f in result.stdout.strip().split('\n')
            if f.strip().endswith('.sql') 
            and not f.startswith('.')
        ]
        
        return modified
    
    except subprocess.CalledProcessError as e:
        print(f"Error comparing with baseline: {e.stderr}", file=sys.stderr)
        return []


def validate_files(files: List[str], is_lab_07: bool = False) -> List[ValidationResult]:
    """Validate syntax of SQL files."""
    results = []
    
    for file_path_str in files:
        file_path = Path(file_path_str)
        
        if not file_path.exists():
            results.append(ValidationResult(
                file=file_path_str,
                valid=False,
                errors=[],
                parser_used=None
            ))
            continue
        
        if is_lab_07:
            result = validate_basic_sql(file_path)
        else:
            result = validate_sql_syntax(file_path, try_mysql=True, try_postgres=True)
        
        results.append(result)
    
    return results


def generate_markdown_report(config: TestConfig, report: TestReport) -> str:
    """Generate comprehensive markdown report."""
    lines = []
    
    lines.append("## Submission Test Results\n")
    
    if report.passed:
        lines.append("### Status: PASSED\n")
    else:
        lines.append("### Status: FAILED (Non-blocking)\n")
    
    lines.append(f"**Lab**: {config.lab_branch}")
    lines.append(f"**Completion**: {report.modified_files}/{report.total_files} files ({report.completion_ratio:.1%})")
    lines.append(f"**Threshold**: {config.completion_threshold:.0%}")
    lines.append(f"**Syntax Errors**: {report.errors_count}\n")
    
    if report.completion_ratio < config.completion_threshold and not config.is_lab_07:
        lines.append(f"**Warning**: Completion ratio below threshold ({report.completion_ratio:.1%} < {config.completion_threshold:.0%})\n")
    
    if report.validation_results:
        lines.append("---\n")
        lines.append("### Validation Details\n")
        
        passed_files = [r for r in report.validation_results if r.valid]
        failed_files = [r for r in report.validation_results if not r.valid]
        
        if passed_files:
            lines.append(f"#### Passed ({len(passed_files)} files)\n")
            for result in passed_files:
                parser_info = f" ({result.parser_used})" if result.parser_used else ""
                lines.append(f"- `{result.file}`{parser_info}")
            lines.append("")
        
        if failed_files:
            lines.append(f"#### Failed ({len(failed_files)} files)\n")
            for result in failed_files:
                lines.append(f"\n**`{result.file}`**")
                if result.errors:
                    for error in result.errors:
                        line_info = f" (line {error.line})" if error.line else ""
                        lines.append(f"- [{error.parser}]{line_info}: {error.message}")
                else:
                    lines.append("- File not found or inaccessible")
            lines.append("")
    
    lines.append("---\n")
    lines.append("_Note: Test failures do NOT block merge. You can still merge this PR with `@bot-s-m-quadri merge`._")
    
    return '\n'.join(lines)


def run_tests(config: TestConfig) -> TestReport:
    """Execute all tests and generate report."""
    print(f"Fetching baseline from {config.lab_branch}...", file=sys.stderr)
    baseline_files = fetch_baseline_files(config.lab_branch)
    
    print(f"Comparing modified files...", file=sys.stderr)
    modified_files = get_modified_files(config.lab_branch)
    
    total_files = len(baseline_files) if not config.is_lab_07 else len(modified_files)
    completion_ratio = len(modified_files) / total_files if total_files > 0 else 0.0
    
    print(f"Validating {len(modified_files)} files...", file=sys.stderr)
    validation_results = validate_files(modified_files, config.is_lab_07)
    
    errors_count = sum(len(r.errors) for r in validation_results)
    
    passed = True
    if not config.is_lab_07 and completion_ratio < config.completion_threshold:
        passed = False
    if errors_count > 0:
        passed = False
    
    return TestReport(
        total_files=total_files,
        modified_files=len(modified_files),
        completion_ratio=completion_ratio,
        validation_results=validation_results,
        passed=passed,
        errors_count=errors_count
    )


def main():
    args = parse_arguments()
    
    config = get_lab_config(args.lab_branch, args.threshold)
    
    print(f"Testing submission for {config.lab_branch}...", file=sys.stderr)
    print(f"Lab 07 mode: {config.is_lab_07}", file=sys.stderr)
    
    report = run_tests(config)
    
    markdown = generate_markdown_report(config, report)
    print(markdown)
    
    sys.exit(0 if report.passed else 1)


if __name__ == '__main__':
    main()
