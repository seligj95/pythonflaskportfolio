pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'echo Building ...'
      }
    }

    stage('test') {
      steps {
        sh 'echo Testing ...'
      }
    }

    stage('Deploy') {
      steps {
        sh '''cd /var/www/html/python-portfolio/
git pull origin dev'''
      }
    }

  }
  triggers {
    cron('H/5 * * * *')
  }
}