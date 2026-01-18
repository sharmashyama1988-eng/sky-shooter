# Sky Shooter

Playable prototype scaffold for Sky Shooter — a mobile-friendly shooter with approachable controls and stunning visuals.

Quick summary
- Engine: Unity (recommend Unity 2022 LTS)
- Target: WebGL demo (for immediate public playability), mobile builds later (Android/iOS)
- Art: Royalty-free placeholder assets (replace with final art later)
- Levels: Level system scaffold included — expand to 70+ levels iteratively

Getting started (local)
1. Install Unity 2022 LTS and open this folder as a Unity project.
2. Create a scene `Assets/Scenes/Main.unity`, add Player prefab and Enemy prefab and wire scripts from `Assets/Scripts`.
3. To test in browser: File → Build Settings → WebGL → Build. Put the build output in `/Builds/WebGL`.

Create the GitHub repo and push (quick)
1. (Optional) Install GitHub CLI: https://cli.github.com/
2. Run:
   - gh repo create sharmashyama1988-eng/sky-shooter --public --confirm
   - git init
   - git add .
   - git commit -m "Initial Sky Shooter scaffold"
   - git branch -M main
   - git remote add origin https://github.com/sharmashyama1988-eng/sky-shooter.git
   - git push -u origin main

Publish WebGL demo (Option A — local build)
1. Build WebGL locally in Unity.
2. Create gh-pages branch and push build:
   - git checkout --orphan gh-pages
   - Remove files except your WebGL build output and an index.html pointing to the build
   - git add . && git commit -m "Deploy WebGL"
   - git push --force origin gh-pages
3. In GitHub → Repo Settings → Pages, choose `gh-pages` branch. Demo will be served from there.

Publish WebGL demo (Option B — GitHub Actions)
- Use the included workflow `.github/workflows/unity-webgl-build.yml`. This automates building Unity WebGL and publishing to the `gh-pages` branch.
- You must set repository secrets for Unity activation (see the workflow comments below).

Git LFS
- If you add large binaries (textures, models), run:
  - git lfs install
  - git lfs track "*.png" "*.jpg" "*.psd" "*.fbx" "*.wav"
  - git add .gitattributes

License
- Default: MIT (see LICENSE file)

If you want, I’ll:
- Walk you through a local build step-by-step
- Help set up the GitHub Actions secrets and enable the workflow
- Prepare a zip with a WebGL build you can directly upload to gh-pages (if you prefer not to use Actions)
