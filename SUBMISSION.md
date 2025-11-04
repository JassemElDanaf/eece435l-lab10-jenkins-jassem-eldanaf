# Lab 10 — Jenkins Submission Checklist

Use this checklist to ensure you’ve met the common grading points. Attach screenshots where indicated.

## Links
- Repo URL: https://github.com/JassemElDanaf/eece435l-lab10-jenkins-jassem-eldanaf

## Jenkins job
- Job type: Pipeline (from SCM)
- Script Path: Jenkinsfile
- Trigger: Poll SCM (H/5 * * * *) or GitHub Webhook (specify which)

## Evidence (add screenshots)
1) Jenkins → Job → Stages view (successful pipeline)
2) Console Output (top + test summary)
3) Test Result (shows 1 test passing)
4) Artifacts page (shows `dist/artifact.txt`)

## Notes (brief)
- Tools configured: NodeJS tool name in Jenkins = `Node18`
- Any issues you solved (e.g., credentials, path quoting, Java version)
- Trigger used and why (poll vs webhook)

## Appendix (optional)
- Jenkinsfile highlights
- Project structure and scripts
