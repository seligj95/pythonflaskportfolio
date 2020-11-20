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
      when { branch 'master' }
      steps {
        sh '''cd /var/www/html/python-portfolio/
git pull origin master'''
      }
        when { branch 'dev' }
      steps {
        sh '''cd /var/www/html/dev/python-portfolio/
git pull origin dev'''
      }
    }

  }
  triggers {
        pollSCM('')
  }
}
