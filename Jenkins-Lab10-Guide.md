# Lab 10 — Jenkins on Windows: What to Do

This guide walks you through what to do for a typical Jenkins lab on Windows. It’s tailored to the PDF you added (which links to the Jenkins Windows installer and docs). If your course requires specific extras, tell me and I’ll adapt.

## 1) Prerequisites
- Windows 10/11 with admin rights
- Git for Windows
- Java JDK 17 (recommended for current Jenkins LTS)
- Your project repo (GitHub or similar)
- Build tool for your stack:
  - Java: Maven or Gradle
  - Node: Node.js + npm
  - Python: Python 3.10+ and pytest

Quick checks:
```powershell
java -version
git --version
mvn -version   # if Maven
gradle -v      # if Gradle
node -v        # if Node.js
python --version  # if Python
```

## 2) Install Jenkins (Windows)
- Download Jenkins LTS MSI: https://www.jenkins.io/download/thank-you-downloading-windows-installer-stable/
- Install with defaults (runs as a Windows Service)
- Open: http://localhost:8080
- Unlock with the admin password shown on screen (usually at `C:\Program Files\Jenkins\secrets\initialAdminPassword`)
- Choose “Install suggested plugins”
- Create the first admin user

Windows install docs (reference): https://www.jenkins.io/doc/book/installing/windows/

## 3) Configure global tools in Jenkins
Jenkins → Manage Jenkins → Tools:
- JDK: point to your local JDK 17 (name it `JDK17`)
- Maven: add a Maven install (name `Maven3`) if using Maven
- Gradle: add if using Gradle
- NodeJS: add if using Node (e.g., `Node18`)

Jenkins → Manage Jenkins → Plugins:
- Ensure Git and Pipeline plugins are installed
- Optional: Pipeline Stage View, Blue Ocean

## 4) Connect Jenkins to your repo
- New Item → Pipeline → name it (e.g., `lab10-pipeline`)
- Definition: “Pipeline script from SCM”
- SCM: Git → enter your repo URL
- Credentials: add/select if private repo (GitHub username + PAT)
- Branch: main (or as needed)
- Script Path: `Jenkinsfile`
- Build Triggers: choose one
  - Poll SCM: `H/5 * * * *` (poll every ~5 min)
  - Or GitHub webhook: http://<your_jenkins_host>:8080/github-webhook/

## 5) Add a Jenkinsfile (choose your stack)
Create `Jenkinsfile` at your repo root and commit. On Windows agents, prefer `bat` over `sh`.

### A) Java + Maven (Windows agent)
```groovy
pipeline {
  agent any
  tools { jdk 'JDK17'; maven 'Maven3' }
  options { timestamps(); ansiColor('xterm') }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Build')    { steps { bat 'mvn -B -DskipTests=false clean package' } }
    stage('Test') {
      steps { bat 'mvn -B test' }
      post { always { junit allowEmptyResults: true, testResults: 'target/surefire-reports/*.xml' } }
    }
    stage('Archive')  { steps { archiveArtifacts artifacts: 'target/**/*.jar', fingerprint: true } }
  }
}
```

### B) Node.js + npm (Windows agent)
```groovy
pipeline {
  agent any
  tools { nodejs 'Node18' }
  options { timestamps(); ansiColor('xterm') }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Install')  { steps { bat 'npm ci' } }
    stage('Test')     { steps { bat 'npm test -- --ci' } }
    stage('Build')    { steps { bat 'npm run build' } }
    stage('Archive')  { steps { archiveArtifacts artifacts: 'dist/**/*', fingerprint: true } }
  }
}
```

### C) Python + pytest (Windows agent)
```groovy
pipeline {
  agent any
  options { timestamps(); ansiColor('xterm') }
  environment { VENV = '.venv' }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Setup') {
      steps {
        bat 'python -m venv .venv'
        bat '.venv\\Scripts\\pip install --upgrade pip'
        bat '.venv\\Scripts\\pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps { bat '.venv\\Scripts\\pytest --junitxml=test-results\\results.xml' }
      post { always { junit 'test-results/results.xml' } }
    }
    stage('Archive') { steps { archiveArtifacts artifacts: 'test-results/**/*.xml', fingerprint: true } }
  }
}
```

## 6) Run and verify
- Build Now (or push a commit to trigger)
- Check Console Output for logs
- Confirm “Test Result” tab shows tests
- Confirm artifacts appear under Artifacts (e.g., JAR or dist/ or test XML)

## 7) What to submit (typical)
- Link to your repo (Jenkinsfile at root)
- Screenshots:
  - Pipeline Stages view showing success
  - Console Output summary
  - Test report and Artifacts
- Short note: which trigger you used (webhook vs poll) and any issues solved

## 8) Troubleshooting (Windows)
- "sh not found": use `bat` steps on Windows agents
- Java/Jenkins mismatch: use JDK 17
- Private repo: add credentials in Jenkins and select them in SCM
- Webhook not firing: ensure Jenkins is reachable from GitHub; otherwise use Poll SCM
- Paths with spaces: quote paths in `bat` commands
- Tests not showing: check the `junit` file pattern matches your project

---
If your lab instructions require exact plugins, a freestyle job instead of Pipeline, or a different toolchain, paste that snippet and I’ll update this guide and the Jenkinsfile accordingly.
