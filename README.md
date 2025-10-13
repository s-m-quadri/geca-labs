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

## Personalized Writeups

Generate concise, thought-heavy lab writeups (Labs 00–10) for each student.

Each writeup has four sections per lab:
1. Subjective (short theory)
2. Objective (short answers, numeric)
3. Code Digest (hand-run on personalized inputs)
4. Conclusion (summary of learnings)

**Following is a quick use for script: `automation-scripts/gen_writeup.py`.**

Preview for first 2 students (no PDF compile):

```bash
python3 automation-scripts/gen_writeup.py --limit 2
```

Generate all and compile to PDFs (requires pdflatex):

```bash
python3 automation-scripts/gen_writeup.py --compile
```

Only specific PRNs

```bash
python3 automation-scripts/gen_writeup.py --only BT23F05F002 BT23F05F010 --compile
```

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
