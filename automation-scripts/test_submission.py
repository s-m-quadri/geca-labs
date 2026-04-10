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
    baseline_files: List[str]
    extra_files: List[str]
    missing_files: List[str]


def parse_arguments():
    parser = argparse.ArgumentParser(description='Test DBMS lab submission')
    parser.add_argument('--lab-branch', required=True, help='Lab branch name (e.g., lab-dbms-04)')
    parser.add_argument('--threshold', type=float, default=0.75, help='Completion threshold (default: 0.75)')
    parser.add_argument('--prn', required=True, help='Student PRN (e.g., BT23F05F001)')
    parser.add_argument('--author', required=True, help='GitHub username of PR author')
    parser.add_argument('--head-repo', required=True, help='Student fork repo (user/repo)')
    parser.add_argument('--head-branch', required=True, help='Student branch name')
    parser.add_argument('--base-repo', required=True, help='Base repository (s-m-quadri/geca-labs)')
    parser.add_argument('--pr-number', required=True, help='PR number')
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


def generate_markdown_report(config: TestConfig, report: TestReport, args) -> str:
    """Generate comprehensive markdown report."""
    now_ist = subprocess.run(
        ['date', '+%d %B %Y, %I:%M %p IST'],
        capture_output=True,
        text=True,
        env={'TZ': 'Asia/Kolkata'}
    ).stdout.strip()
    
    lines = []
    
    lines.append(f"### PRN: <a href=\"https://github.com/{args.base_repo}/pulls?q={args.prn}\" target=\"_blank\"><code>{args.prn}</code></a> Test Results\n")
    
    if report.passed:
        lines.append("**Validation Status**: PASSED")
        lines.append("\nYour submission meets the minimum requirements for syntax and completion. Great work!\n")
    else:
        lines.append("**Validation Status**: FAILED (Non-blocking)")
        lines.append("\nYour submission has some issues that need attention. Please review the details below and consider making improvements before the final review.\n")
    
    lines.append("> [!NOTE]")
    lines.append(f"> - Test Date: **{now_ist}**")
    lines.append(f"> - Lab: **{config.lab_branch}**")
    lines.append(">")
    lines.append("> | Info. | Value/Link |")
    lines.append("> |-----------------:|:------|")
    lines.append(f"> | PRN | <a href=\"https://github.com/{args.base_repo}/pulls?q={args.prn}\" target=\"_blank\"><b>{args.prn}</b></a> (All submissions) |")
    
    lab_num = config.lab_number
    subject = config.lab_branch.split('-')[1] if '-' in config.lab_branch else 'dbms'
    lines.append(f"> | Lab Number | <a href=\"https://www.s-m-quadri.me/geca/{subject}/{lab_num}\" target=\"_blank\"><b>{lab_num}</b></a> (Manual) |")
    lines.append(f"> | Problem Set | <a href=\"https://github.com/{args.base_repo}/tree/{config.lab_branch}\" target=\"_blank\"><b>{config.lab_branch}</b></a> (View baseline) |")
    lines.append(f"> | Your Repository | <a href=\"https://github.com/{args.head_repo}\" target=\"_blank\"><b>{args.head_repo}</b></a> (Your fork) |")
    lines.append(f"> | Your Branch | <a href=\"https://github.com/{args.head_repo}/tree/{args.head_branch}\" target=\"_blank\"><b>{args.head_branch}</b></a> (Resume work) |")
    lines.append(f"> | Pull Request | <a href=\"https://github.com/{args.base_repo}/pull/{args.pr_number}\" target=\"_blank\"><b>#{args.pr_number}</b></a> (This PR) |\n")
    
    lines.append("---\n")
    lines.append("### File-by-File Analysis\n")
    
    lines.append("| Problem Set | Your Solution | Syntax Check | Remark | Status |")
    lines.append("|-------------|---------------|--------------|---------|--------|")
    
    baseline_set = set(report.baseline_files)
    modified_dict = {r.file: r for r in report.validation_results}
    modified_set = set(modified_dict.keys())
    
    for baseline_file in sorted(report.baseline_files):
        baseline_url = f"https://github.com/{args.base_repo}/blob/{config.lab_branch}/{baseline_file}"
        baseline_link = f"[`{baseline_file}`]({baseline_url})"
        
        if baseline_file in modified_set:
            result = modified_dict[baseline_file]
            student_url = f"https://github.com/{args.head_repo}/blob/{args.head_branch}/{baseline_file}"
            student_link = f"[`{baseline_file}`]({student_url})"
            
            if result.valid:
                parser_info = f"{result.parser_used}" if result.parser_used else "basic"
                remark = "✓ Syntax OK"
                status = "✓ PASS"
            else:
                error_count = len(result.errors)
                remark = f"{error_count} error(s)"
                status = "✗ FAIL"
            
            lines.append(f"| {baseline_link} | {student_link} | {parser_info} | {remark} | {status} |")
        else:
            lines.append(f"| {baseline_link} | — | — | Not submitted | ⚠ MISSING |")
    
    if report.extra_files:
        lines.append("")
        lines.append("**Extra Files (not in problem set):**\n")
        for extra_file in sorted(report.extra_files):
            result = modified_dict.get(extra_file)
            student_url = f"https://github.com/{args.head_repo}/blob/{args.head_branch}/{extra_file}"
            student_link = f"[`{extra_file}`]({student_url})"
            
            if result and result.valid:
                parser_info = f"{result.parser_used}" if result.parser_used else "basic"
                remark = "✓ Syntax OK"
                status = "✓ PASS"
            elif result:
                error_count = len(result.errors)
                remark = f"{error_count} error(s)"
                status = "✗ FAIL"
            else:
                parser_info = "—"
                remark = "Not validated"
                status = "?"
            
            lines.append(f"| — | {student_link} | {parser_info} | {remark} | {status} |")
    
    lines.append("")
    lines.append("---\n")
    lines.append("### Overall Summary\n")
    
    lines.append(f"- **Completion**: {len(modified_set)}/{len(baseline_set)} files ({report.completion_ratio:.1%})")
    lines.append(f"- **Threshold**: {config.completion_threshold:.0%}")
    lines.append(f"- **Syntax Errors**: {report.errors_count}")
    lines.append(f"- **Extra Files**: {len(report.extra_files)}")
    lines.append(f"- **Missing Files**: {len(report.missing_files)}\n")
    
    if report.passed:
        lines.append("> ✓ **Acceptable**: Your submission is complete and syntactically correct.")
    else:
        lines.append("> ⚠ **Needs Improvement**: Please address the issues listed above.")
        
        if report.completion_ratio < config.completion_threshold and not config.is_lab_07:
            lines.append(f">")
            lines.append(f"> **Warning**: Completion ratio ({report.completion_ratio:.1%}) is below threshold ({config.completion_threshold:.0%}).")
        
        if report.errors_count > 0:
            lines.append(f">")
            lines.append(f"> **Warning**: {report.errors_count} syntax error(s) detected. Please fix them before final submission.")
    
    lines.append("")
    
    if not report.passed:
        lines.append("---\n")
        lines.append("### Suggestions for Improvement\n")
        
        if report.missing_files:
            lines.append(f"- Complete the {len(report.missing_files)} missing file(s) from the problem set")
        
        if report.errors_count > 0:
            lines.append("- Fix all syntax errors shown in the file analysis table above")
            lines.append("- Test your SQL files locally using MySQL/PostgreSQL before committing")
        
        if report.completion_ratio < config.completion_threshold:
            needed = int((config.completion_threshold * len(baseline_set)) - len(modified_set)) + 1
            lines.append(f"- Submit at least {needed} more file(s) to meet the {config.completion_threshold:.0%} threshold")
        
        lines.append("")
    
    lines.append("---\n")
    lines.append("> **Note**: Test failures do NOT block merge. You can merge this PR with `@bot-s-m-quadri merge` even if tests fail. However, incomplete or erroneous submissions may affect your evaluation.\n")
    
    lines.append(f"In case of doubts, contact 📧 **hi@s-m-quadri.me**, or <a href=\"https://github.com/{args.base_repo}/pull/{args.pr_number}\" target=\"_blank\"><b>comment here</b></a>.\n")
    
    if report.passed:
        lines.append("Great work! Keep it up! 🎉")
    else:
        lines.append("Keep improving! 🙂")
    
    return '\n'.join(lines)


def run_tests(config: TestConfig) -> TestReport:
    """Execute all tests and generate report."""
    print(f"Fetching baseline from {config.lab_branch}...", file=sys.stderr)
    baseline_files = fetch_baseline_files(config.lab_branch)
    
    print(f"Comparing modified files...", file=sys.stderr)
    modified_files = get_modified_files(config.lab_branch)
    
    baseline_set = set(baseline_files)
    modified_set = set(modified_files)
    
    extra_files = list(modified_set - baseline_set)
    missing_files = list(baseline_set - modified_set)
    
    total_files = len(baseline_files) if not config.is_lab_07 else len(modified_files)
    completion_ratio = len(modified_set & baseline_set) / total_files if total_files > 0 else 0.0
    
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
        errors_count=errors_count,
        baseline_files=baseline_files,
        extra_files=extra_files,
        missing_files=missing_files
    )


def main():
    args = parse_arguments()
    
    config = get_lab_config(args.lab_branch, args.threshold)
    
    print(f"Testing submission for {config.lab_branch}...", file=sys.stderr)
    print(f"Lab 07 mode: {config.is_lab_07}", file=sys.stderr)
    
    report = run_tests(config)
    
    markdown = generate_markdown_report(config, report, args)
    print(markdown)
    
    sys.exit(0 if report.passed else 1)


if __name__ == '__main__':
    main()
