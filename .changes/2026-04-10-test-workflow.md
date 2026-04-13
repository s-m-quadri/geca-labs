## DBMS Lab Testing Workflow

**Date**: 2026-04-10

### New Files

1. **`.github/workflows/test-submission.yml`**
   - Trigger: PR comment `@bot-s-m-quadri test`
   - Installs MySQL + PostgreSQL clients
   - Runs test script, posts markdown results
   - Updates labels: `🧪 Tests Passed` / `⚠️ Tests Failed (Non-blocking)`

2. **`automation-scripts/test_submission.py`**
   - Orchestrates validation flow
   - Fetches baseline from orphan branch (`lab-dbms-NN`)
   - Compares modified files vs baseline
   - Calculates completion ratio (threshold: 75%)
   - Calls validators for syntax checking
   - Generates comprehensive markdown report (similar to status workflow)
   - Includes file-by-file mapping with GitHub URLs
   - Shows extra files, missing files, and suggestions
   - Exit code: 0 (pass) | 1 (fail, non-blocking)

3. **`automation-scripts/lib/validators.py`**
   - `validate_sql_syntax()`: Try MySQL parser, fallback to PostgreSQL
   - `validate_basic_sql()`: Minimal check for Lab 7 (file exists, has SQL keywords)
   - Returns structured `ValidationResult` with errors (file, line, message, parser)

### Workflow Integration

**Flow**:

```
Student opens PR (lab-dbms-NN <- student-branch)
    ↓
Comments: @bot-s-m-quadri test
    ↓
[test-submission.yml] triggers
    ↓ Checkout stable (get automation-scripts/)
    ↓ Copy automation-scripts/ to /tmp/
    ↓ Checkout PR head + restore automation-scripts/
    ↓ Fetch origin/lab-dbms-NN (baseline)
    ↓ Run test_submission.py --lab-branch lab-dbms-NN
    ↓ Post results as comment
    ↓ Add label (Tests Passed/Failed)
    ↓
Student can still merge: @bot-s-m-quadri merge
    ↓
[merge-organize.yml] runs (unchanged, independent)
```

**Validations**:
| Check | Labs 4-6 | Lab 7 |
|-------|----------|-------|
| Completion ratio (≥75%) | Yes | No |
| SQL syntax (MySQL/PostgreSQL) | Yes | Basic only |
| File existence | Yes | Yes |
| Non-blocking merge | Yes | Yes |

### Usage

**Student**:

```bash
# Open PR from lab-dbms-NN branch
# Comment on PR:
@bot-s-m-quadri test

# Review comprehensive results with:
#   - PRN header with all submission links
#   - File-by-file comparison table (problem set vs your solution)
#   - Syntax check results with hyperlinks to both baseline and your files
#   - Overall summary (completion ratio, errors, missing/extra files)
#   - Suggestions for improvement
#   - Contact information

# Fix errors if needed, then merge when ready (tests don't block):
@bot-s-m-quadri merge
```

**Instructor**:

- Review test results in PR comments
- Comprehensive report shows file-by-file analysis with GitHub links
- Merge regardless of test status if appropriate
- Tests provide feedback, not enforcement

### Configuration

**Adjusting threshold**:
Edit workflow step in `.github/workflows/test-submission.yml`:

```yaml
- name: Run tests
  run: |
    python3 test_submission.py --lab-branch "${LAB_BRANCH}" --threshold 0.80
```

**Per-lab thresholds** (future):
Create `automation-scripts/config/lab_thresholds.json`:

```json
{
  "lab-dbms-04": 0.75,
  "lab-dbms-05": 0.8,
  "lab-dbms-06": 0.7,
  "lab-dbms-07": 0.0
}
```

### Technical Details

**Orphan Branch Handling**:

- DBMS lab branches (`lab-dbms-NN`) are orphan branches with no `automation-scripts/`
- Workflow checks out `stable` branch first to get test scripts
- Copies scripts to `/tmp/`, checks out PR head, then restores scripts
- This ensures both test infrastructure and submission are available

**SQL Validation Strategy**:

1. Try MySQL parser: `mysql --batch -e "DELIMITER //\n{sql}\n//"`
2. If fails, try PostgreSQL: `psql -c "{sql}"`
3. Parse error messages into structured format
4. Lab 7: Skip parsers, only check file has SQL keywords

**Completion Calculation**:

```
baseline_files = files in origin/lab-dbms-NN (exclude *_setup.sql, *check_status.sql)
modified_files = git diff --name-only origin/lab-dbms-NN HEAD (*.sql only)
ratio = len(modified_files & baseline_files) / len(baseline_files)
extra_files = modified_files - baseline_files
missing_files = baseline_files - modified_files
```

**Comprehensive Report Format**:

The test report includes:

1. **Header Section**
   - PRN with link to all submissions
   - Timestamp (IST)
   - Quick-access table with links to:
     - Lab manual
     - Problem set (baseline branch)
     - Student's repository and branch
     - Current PR

2. **File-by-File Analysis Table**

   ```
   | Problem Set | Your Solution | Syntax Check | Remark | Status |
   |-------------|---------------|--------------|---------|--------|
   | [file1.sql] | [file1.sql]   | mysql       | ✓ Syntax OK | ✓ PASS |
   | [file2.sql] | —             | —           | Not submitted | ⚠ MISSING |
   ```

   - Hyperlinks to both baseline and student files on GitHub
   - Parser used (MySQL/PostgreSQL/basic)
   - Error count and status for each file
   - Extra files (not in problem set) listed separately

3. **Overall Summary**
   - Completion ratio vs threshold
   - Total syntax errors
   - Count of extra/missing files
   - Pass/fail verdict with explanation

4. **Suggestions Section**
   - Specific actionable improvements
   - Missing file reminders
   - Syntax error fixing tips

5. **Footer**
   - Non-blocking merge reminder
   - Contact information (email + PR comment link)
   - Encouragement message

### Independence

- **No coupling** with existing workflows
- `test-submission.yml` runs on `@bot test` only
- `merge-organize.yml` unchanged, still triggered by `@bot merge`
- Labels are separate: test labels vs merge labels
- Can skip tests entirely, merge still works

### Future Enhancements

1. Result validation (check row counts, schema)
2. Performance benchmarks (query execution time)
3. Code quality checks (SQL formatting, best practices)
4. Test result persistence (database/CSV for analytics)
5. Per-lab custom validators
