pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'hello'
        sh 'echo hello'
        sh 'git status'
        sh '''cd /var/www/html/python-portfolio/
git pull origin dev'''
      }
    }

  }
  triggers {
    cron('H/5 * * * *')
  }
}