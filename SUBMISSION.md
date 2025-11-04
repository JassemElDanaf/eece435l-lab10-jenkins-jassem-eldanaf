# Lab 10 — Jenkins Submission Checklist

Use this checklist to ensure you’ve met the common grading points. Attach screenshots where indicated.

## Links
- Repo URL: https://github.com/JassemElDanaf/eece435l-lab10-jenkins-jassem-eldanaf

## Jenkins job
- Job type: Pipeline (from SCM)
- Script Path: Jenkinsfile
- Branch: main
- Trigger: Poll SCM (H/5 * * * *) or GitHub Webhook (specify which)

## Evidence (add screenshots)
1) Jenkins → Job → Stages view (successful pipeline)
	- Stages: Checkout SCM, Setup, Lint, Test, Coverage, Security Scan, Deploy, Archive
2) Console Output (top + summary lines for Test, Coverage, Security Scan)
3) Test Result (shows 1 pytest test passing)
4) Artifacts page (shows `dist/artifact.txt`, `coverage.xml`, `bandit.txt`)
5) Tools page (Node18 if used previously is fine; Python uses venv in workspace)

## Notes (brief)
- Pipeline language: Python on Windows using venv
- Lint: flake8; Tests: pytest (JUnit XML published)
- Coverage: coverage.py (XML archived); Security: bandit (report archived)
- Any issues you solved (e.g., installing Python, path quoting)
- Trigger used and why (poll vs webhook)

## Appendix (optional)
- Jenkinsfile highlights
- Project structure and scripts
