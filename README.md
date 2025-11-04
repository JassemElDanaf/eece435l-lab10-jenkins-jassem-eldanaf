# Lab 10 — Jenkins Demo Project

This repo contains a minimal Node.js project and a `Jenkinsfile` for a Windows Jenkins agent.

## Project
- Node.js + Jest tests
- Build produces `dist/artifact.txt` for Jenkins to archive

## Scripts
```bash
npm test   # run unit tests
npm run build  # generate artifact in dist/
```

## Jenkins
- Use the Pipeline job type
- Definition: Pipeline script from SCM, Script Path: `Jenkinsfile`
- Ensure Jenkins has a NodeJS tool named `Node18`
- Stages: Checkout → Install (npm ci) → Test → Build → Archive

## Push to GitHub
1. Create a new empty repo on GitHub (do not add a README/License)
2. Add the remote and push:
```powershell
git remote add origin https://github.com/<your-username>/<your-repo>.git
git branch -M main
git push -u origin main
```

## What to submit
- GitHub repo URL with `Jenkinsfile`
- Screenshots from Jenkins: Stages view, Console Output, Test Results, and Artifacts
- Note whether you used Poll SCM or GitHub webhook
