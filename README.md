# Sky Shooter

Playable prototype scaffold for Sky Shooter.

Quick notes:
- Unity version recommended: 2022.3 LTS (set same version in workflow).
- CI: GitHub Actions workflow present to build WebGL and deploy to gh-pages.
- Unity license (manual) required for Actions to successfully build. Add as repo secret `UNITY_LICENSE` later.

How to run CI (summary):
1. Push this workflow to `main`.
2. Add Unity license secret (when available): Settings → Secrets & variables → Actions → New repository secret → Name = UNITY_LICENSE (base64 of your Unity license file).
3. Trigger workflow from Actions tab or push a new commit.

If you prefer immediate demo without CI:
- Build WebGL locally in Unity and deploy to `gh-pages` branch manually (see deployment steps in repo docs).