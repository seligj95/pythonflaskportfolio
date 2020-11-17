pipeline {
  agent any
  triggers {
        cron('H/5 * * * *')
    }
  stages {
    stage('build') {
      steps {
        echo 'hello'
        sh 'echo hello'
        sh 'git status'
      }
    }

  }
}
