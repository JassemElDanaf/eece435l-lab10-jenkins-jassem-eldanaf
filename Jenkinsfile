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
  post {
    always { echo "Build finished: ${currentBuild.currentResult}" }
  }
}
