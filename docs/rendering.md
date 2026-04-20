Rendering Guide
Tips, tricks, and common commands for rendering the SynapticByte animations.
---
Quality presets
Manim ships with four quality flags. Pick based on what you're doing:
Flag	Resolution	FPS	Use case
`-ql`	480p	15	Fast iteration while developing a scene
`-qm`	720p	30	Casual preview, sharable drafts
`-qh`	1080p	60	Default for most work
`-qk`	2160p (4K)	60	Final YouTube upload; slow render
The `-p` flag opens the video automatically after rendering:
```bash
manim -pqh 01_logic_of_uncertainty/logic_of_uncertainty.py LogicOfUncertainty
```
---
Rendering individual scenes
Each script is organized as one top-level class with many `scene_*` methods. To render a single method in isolation, create a small wrapper at the bottom of the script:
```python
class JustTheBirthdayHook(LogicOfUncertainty):
    def construct(self):
        self.camera.background_color = DARK_BG
        self.scene_birthday_hook()
```
Then render that class:
```bash
manim -pqh 01_logic_of_uncertainty/logic_of_uncertainty.py JustTheBirthdayHook
```
This is the fastest way to iterate on a single visual without re-rendering the full video.
---
Rendering a still frame
Use `-s` to save only the final frame as a PNG. Useful for thumbnails, slides, or debugging the final layout of a scene:
```bash
manim -pqh -s 02_soul_of_statistics/soul_of_statistics.py SoulOfStatistics
```
---
Transparent backgrounds
For compositing frames into other software (Final Cut, Premiere, After Effects), render with an alpha channel:
```bash
manim -pqh --transparent 01_logic_of_uncertainty/logic_of_uncertainty.py LogicOfUncertainty
```
The output is a `.mov` with transparency preserved.
---
Where renders are saved
By default, Manim writes output to:
```
media/videos/<script_name>/<resolution>/<SceneName>.mp4
```
For example, a high-quality render of `LogicOfUncertainty` lands at:
```
media/videos/logic_of_uncertainty/1080p60/LogicOfUncertainty.mp4
```
The whole `media/` folder is gitignored.
---
Performance tips
Disable the partial movie cache for a one-off fresh render: `--disable_caching`.
Flush all caches if you hit weird stale-mobject bugs: `manim --flush_cache`.
Use the OpenGL renderer for interactive development: `--renderer=opengl`. It's faster and lets you navigate the scene with the mouse, but some features (especially 3D transforms and certain TeX compositions) behave differently, so always do the final render with the default Cairo renderer.
Heavy LaTeX scenes are slow. The first render compiles every unique `MathTex` expression; subsequent renders reuse the cache. Don't worry about the first render taking much longer than the second.
---
Missing SVG assets
Every `SVGMobject(...)` call in the scripts is wrapped in a `try/except`. If the asset is missing, the scene falls back to a simple geometric shape and the animation still renders — just with less polish.
If you want to replace the placeholders, drop properly-licensed SVGs (e.g. from Feather Icons, Heroicons, or Tabler Icons) into the corresponding video's `assets/` folder with the filenames referenced in the script. The scripts load assets by relative path, so they resolve against Manim's working directory — run `manim` from the repo root for the paths to work.
---
Common gotchas
`TeX compilation error` — usually a LaTeX package missing. Ensure `dvisvgm`, `standalone`, and the default Manim TeX packages are installed. On Ubuntu: `sudo apt install texlive-latex-extra texlive-fonts-extra dvisvgm`.
`FileNotFoundError: ffmpeg` — install FFmpeg and make sure it's on your PATH.
Scene plays too fast / out of order — check that your `self.play(...)` and `self.wait(...)` calls aren't nested inside another `self.play(...)`. Manim only plays animations at the outermost `play()` level.
Colors look off — verify you're importing from `shared.palette` rather than using Manim's built-in named colors. The 3B1B-style palette is deliberately different from Manim defaults.
