# GECA Labs

This repository provides a structured collection of laboratory resources for advanced undergraduate and postgraduate courses in Computer Science and Engineering.  

The materials are authored and maintained on [https://www.s-m-quadri.me/geca](https://www.s-m-quadri.me/geca), a personal academic site that hosts lab manuals and supporting resources. While the author is affiliated with Government College of Engineering, Aurangabad (GECA), this is not an official institutional repository.

## History Visualization

Run the following commands to generate a visual representation of the repository's history:

```sh
gource --title "s-m-quadri/geca-labs" --start-date "2025-07-15 00:00:00" --viewport 1920x1080 --output-ppm-stream dump.ppm  --highlight-users --auto-skip-seconds 1 --seconds-per-day 1 --user-scale 1 --bloom-multiplier 1.0 --bloom-intensity 0.5 --key --hide progress --colour-images --filename-colour FFD700 --dir-colour FFD700 --background-colour 1a1a00 --font-colour FFFFFF --highlight-colour FFFFFF --follow-user "USERNAME" --camera-mode track
```

Then convert the output to a video file using ffmpeg

```sh
ffmpeg -y -r 25 -f image2pipe -vcodec ppm -i dump.ppm -c:v libx265 -preset slow -pix_fmt yuv420p -crf 30 -bf 0 out.mp4
```

## Automation Scripts

Public scripts live in `automation-scripts/` (Python files not ignored by git). Below is a terse guide with typical flags. Run any script with `-h` to see full options.

- **Generate covers** (LaTeX/PDF) per student/lab: `automation-scripts/gen_cover.py`
  - Inputs: `automation-scripts/output/students.csv`, `automation-scripts/output/commits.csv`
  - Default output: `automation-scripts/output/daa-covers/{PRN}/...`
  - Examples:
    - Preview for specific PRNs and labs (no PDF):
      - `python3 automation-scripts/gen_cover.py --only BT23F05F002 BT23F05F013 --labs 0 1`
    - Generate all with PDFs (requires pdflatex):
      - `python3 automation-scripts/gen_cover.py --compile`

- **Generate writeups** (LaTeX/PDF): `automation-scripts/gen_writeup.py`
  - Examples:
    - Preview first N students: `python3 automation-scripts/gen_writeup.py --limit 2`
    - Generate all + PDF: `python3 automation-scripts/gen_writeup.py --compile`

- **Fetch pull requests metadata**: `automation-scripts/fetch_pull_requests.py`
  - Produces: `automation-scripts/output/pull_requests.csv/.xlsx` and raw commit artifact files
  - Example: `python3 automation-scripts/fetch_pull_requests.py`

- **Check pull requests** (simple report): `automation-scripts/check_pull_requests.py`
  - Reads previously fetched artifacts and prints a summary
  - Example: `python3 automation-scripts/check_pull_requests.py`

- **Attendance sheet** from commits: `automation-scripts/gen_attendance.py`
  - Produces: `automation-scripts/output/attendance.(csv|xlsx)` and `students.(csv|xlsx)` if needed
  - Example: `python3 automation-scripts/gen_attendance.py`

- **Lab summary report** (PDF): `automation-scripts/gen_report.py`
  - Produces: `automation-scripts/output/report-*.pdf`
  - Example: `python3 automation-scripts/gen_report.py`

- **Misc student utilities**: `automation-scripts/misc_students.py`
  - Grab-bag helpers (IDs, quick transformations)
  - Example: `python3 automation-scripts/misc_students.py -h`

> [!NOTE]
> - Some scripts depend on `pdflatex` (TeX Live) to compile PDFs. If unavailable, run without `--compile` or install a LaTeX distribution.
> - CSVs live under `automation-scripts/output/` and are produced by `fetch_pull_requests.py` and related scripts.
> - Use `--only <PRN ...>` and `--labs <numbers>` to scope work.

## Objective

- Facilitate **hands-on laboratory education** in key domains of Computer Science.
- Provide **well-structured practical documentation** for academic use.
- Promote **reproducibility and clarity** through openly licensed and organized resources.

## License

This repository is licensed under the GPL-3.0 license. See the [LICENSE](./LICENSE) file for details.

## Contributors and Learners

The repository is authored and maintained primarily by the owner, with contributions from students, colleagues, and collaborators from GECA and other institutions.

<a href="https://github.com/s-m-quadri/geca-labs/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=s-m-quadri/geca-labs&anon=1" />
</a>
