# SynapticByte

> Visual intuition for the math behind intelligence, built with Manim.

This repository contains the full Manim source code for every animation published on the [**SynapticByte**](https://www.youtube.com/channel/UCz9OT1Rcx5MgUDxK4fsMXOQ) YouTube channel. Each video is a self-contained, fully-reproducible explainer covering topics across probability, statistics, linear algebra, and the mathematics of machine learning.

Created by [Chaouki Ben Issaid](https://github.com/) — Senior Researcher and Adjunct Professor at the University of Oulu, specializing in federated learning, distributed optimization, and wireless communications.

---

## Videos in this repository

| № | Video | Folder | YouTube |
|---|---|---|---|
| 01 | Probability & Combinatorics, Visually Explained | [`01_logic_of_uncertainty/`](./01_logic_of_uncertainty) | [Watch](https://www.youtube.com/watch?v=AZKP7mejviQ) |
| 02 | Conditional Probability — The Soul of Statistics | [`02_soul_of_statistics/`](./02_soul_of_statistics) | *(coming soon)* |
| 03 | The Laplace Transform, Visually Explained | [`03_laplace_blueprint/`](./03_laplace_blueprint) | *(coming soon)* |

Each video folder contains its own README with a scene-by-scene breakdown, required assets, and rendering instructions specific to that video.

---

## Quick start

### Requirements

- Python 3.9+
- [Manim Community Edition](https://docs.manim.community/en/stable/installation.html) (v0.18+)
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX) for rendered math

### Installation

```bash
# Clone the repo
git clone https://github.com/<your-username>/synapticbyte.git
cd synapticbyte

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

For Manim's system-level dependencies (FFmpeg, Cairo, Pango), follow the [official installation guide](https://docs.manim.community/en/stable/installation.html) for your OS.

### Render a video

Each video has a single top-level scene class. From the repo root:

```bash
# Render at preview quality (720p, fast)
manim -pql 01_logic_of_uncertainty/logic_of_uncertainty.py LogicOfUncertainty

# Render at production quality (1080p60)
manim -pqh 01_logic_of_uncertainty/logic_of_uncertainty.py LogicOfUncertainty

# Render at 4K (slow; for the final YouTube upload)
manim -pqk 01_logic_of_uncertainty/logic_of_uncertainty.py LogicOfUncertainty
```

You can also render individual methods of a scene by extracting them — see [`docs/rendering.md`](./docs/rendering.md) for details.

### Render a single scene only

The `-s` flag saves only the last frame, useful for iterating on a specific visual:

```bash
manim -pqh -s 02_soul_of_statistics/soul_of_statistics.py SoulOfStatistics
```

---

## Repository structure

```
synapticbyte/
├── shared/                       # Reusable components across all videos
│   ├── palette.py                #   3B1B-inspired color constants
│   ├── components.py             #   Pebble, section_title, golden_box, ...
│   └── __init__.py
│
├── 01_logic_of_uncertainty/      # Video 01 — probability & combinatorics
│   ├── logic_of_uncertainty.py
│   ├── assets/                   #   SVG files (placeholders)
│   └── README.md
│
├── 02_soul_of_statistics/        # Video 02 — conditional probability
│   ├── soul_of_statistics.py
│   ├── assets/
│   └── README.md
│
├── 03_laplace_blueprint/         # Video 03 — the Laplace transform
│   ├── laplace_blueprint.py
│   ├── assets/
│   └── README.md
│
├── docs/
│   └── rendering.md              # rendering tips and settings
│
├── requirements.txt
├── LICENSE
├── CITATION.cff
└── README.md                     # this file
```

---

## A note on audio and voiceover

The scripts in this repo are the **raw, silent versions** of the animations. The narrated voiceovers heard on the YouTube channel are generated separately using a text-to-speech pipeline and synchronized at render time in the production version of each script. They are not included here.

If you want to add your own narration, each scene's animations are cleanly separated — you can use a voiceover extension like [`manim-voiceover`](https://voiceover.manim.community/) to wrap each `self.play(...)` call with synchronized audio.

---

## Assets

The `assets/` folder inside each video contains placeholder SVG files. **You will need to provide your own icons** (or replace the `SVGMobject(...)` calls with code-drawn alternatives). Every scene that loads an SVG is wrapped in a `try/except` so missing assets will fall back to simple geometric shapes and the animation will still render cleanly — just with less polish.

Recommended free sources for replacement SVGs:
- [Feather Icons](https://feathericons.com/) (MIT license)
- [Heroicons](https://heroicons.com/) (MIT license)
- [Tabler Icons](https://tabler-icons.io/) (MIT license)
- [The Noun Project](https://thenounproject.com/) (attribution required)

---

## Credits & inspiration

The visual style of these animations is heavily inspired by [**3Blue1Brown**](https://www.3blue1brown.com/) (Grant Sanderson), whose channel first showed the world what programmatic math animation could become. The [Manim Community](https://www.manim.community/) is responsible for maintaining the open-source animation engine that makes all of this possible.

If you enjoy this work, consider:
- Subscribing to [SynapticByte on YouTube](https://www.youtube.com/channel/UCz9OT1Rcx5MgUDxK4fsMXOQ)
- Starring this repository
- Opening an issue or pull request if you find a bug or want to improve a scene

---

## License

The **code** in this repository is released under the [MIT License](./LICENSE). You are free to use, modify, and redistribute it, including for commercial purposes, provided that you include the original copyright notice.

The **rendered video outputs** (the finished animations published on YouTube) are not covered by this license and remain © Chaouki Ben Issaid. Please do not reupload them.

---

## Citation

If you use these animations in your own teaching, research, or derivative work, a citation is appreciated but not required. See [`CITATION.cff`](./CITATION.cff) for a machine-readable citation entry, or use:

> Ben Issaid, C. (2026). *SynapticByte: Visual intuition for the math behind intelligence.* GitHub repository. https://github.com/&lt;your-username&gt;/synapticbyte
