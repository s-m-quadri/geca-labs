# GECA Labs

This repository hosts a structured collection of laboratory resources aligned with advanced undergraduate and postgraduate coursework in Computer Science and Engineering. The materials are curated and adapted from GECA Aurangabad's official instructional site: [https://www.s-m-quadri.me/geca](https://www.s-m-quadri.me/geca).

## Visualization

Run the following commands to generate a visual representation of the repository's history:

```sh
gource --title "s-m-quadri/geca-labs" --start-date "2025-07-15 00:00:00" --viewport 1920x1080 --output-ppm-stream dump.ppm --background-colour 1a1a00 --font-colour FFD700 --highlight-users --highlight-colour FF0000  --auto-skip-seconds 1 --seconds-per-day 1 --user-scale 1 --bloom-multiplier 0.5 --bloom-intensity 0.5 --key --hide progress
```

Then convert the output to a video file using ffmpeg

```sh
ffmpeg -y -r 25 -f image2pipe -vcodec ppm -i dump.ppm -vcodec libx264 -preset ultrafast -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 out.mp4
```

## Objective

- Facilitate **hands-on laboratory education** in key domains of Computer Science.
- Provide **well-structured practical documentation** for academic use.
- Promote **reproducibility and clarity** through openly licensed and organized resources.

## License

This repository is licensed under the GPL-3.0 license. See the [LICENSE](./LICENSE) file for details.

## Contributors and Learners

<a href="https://github.com/s-m-quadri/geca-labs/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=s-m-quadri/geca-labs&anon=1" />
</a>
