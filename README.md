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

All scripts live in `automation-scripts/`. Require `GITHUB_TOKEN` env var for API calls. Run any script with `-h` for full options.

### Typical workflow

```sh
cd automation-scripts

# 1. Fetch detailed PR data (incremental/resumable, per course)
python3 fetch_pr.py --course dbms
python3 fetch_pr.py --course daa

# 2. Validate submissions (identity clashes, open/merged conflicts, filesystem checks)
python3 check_pull_requests.py --course dbms
python3 check_pull_requests.py --course daa --no-fs

# 3. Interactive PR console (review, approve, post comments)
python3 pr_console.py --course dbms --live

# 4. Generate attendance sheet from commits
python3 gen_attendance.py --course dbms

# 5. Generate cover pages (requires pdflatex)
python3 gen_cover.py --course dbms --compile
# or preview for specific PRNs/labs only:
python3 gen_cover.py --course dbms --only BT24F05F001 --labs 1 2

# 6. Generate writeups (requires pdflatex)
python3 gen_writeup.py --course dbms --compile

# 7. Generate lab summary report (PDF)
python3 gen_report.py --course dbms
```

### Key flags

| Flag                 | Description                                       |
| -------------------- | ------------------------------------------------- |
| `--course dbms\|daa` | Select course (required for most scripts)         |
| `--only <PRN ...>`   | Scope to specific roll numbers                    |
| `--labs <N ...>`     | Scope to specific lab numbers                     |
| `--force`            | Re-fetch even if cached (`fetch_pr.py`)           |
| `--no-fs`            | Skip filesystem checks (`check_pull_requests.py`) |
| `--compile`          | Compile LaTeX to PDF                              |

### Outputs

| Path                              | Content                                          |
| --------------------------------- | ------------------------------------------------ |
| `output/{course}/pr_details.json` | Full PR data — commits, files, comments, reviews |
| `output/{course}/attendance.csv`  | Attendance from commits                          |
| `output/{course}/covers/`         | Per-student cover page PDFs                      |
| `output/{course}/report-*.pdf`    | Lab summary report                               |

> [!NOTE]
> `pdflatex` (TeX Live) required for `--compile`. Without it, LaTeX source is still generated.

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
