pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'hello'
        sh 'echo hello'
        sh 'git status'
        sh '''cd /var/www/html/python-portfolio/
sudo git pull origin dev
sudo git status'''
      }
    }

  }
  triggers {
    cron('H/5 * * * *')
  }
}