pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'hello'
        sh 'echo hello'
        sh 'git status'
        sh 'ls'
      }
    }

  }
  triggers {
    cron('H/5 * * * *')
  }
}