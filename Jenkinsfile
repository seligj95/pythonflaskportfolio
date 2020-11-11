pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building'
        sh '''jenkins/workspace/build.sh
'''
      }
    }

    stage('Test') {
      steps {
        echo 'Testing'
        sh 'jenkins/workspace/test-all.sh'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying'
        sh 'jenkins/workspace/deploy.sh'
      }
    }

  }
}