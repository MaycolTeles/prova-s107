pipeline {
  agent any

  environment {
    EMAIL = 'jv.oliveirag@gmail.com'
  }

  stages {
    stage('Test') {
      steps {
        echo 'Testing...'
        sh 'ls'
        sh 'pwd'
        sh 'cd backend'
        sh 'pip install --upgrade pip'
        sh 'pip install -r requirements.txt'
        sh 'pytest -vv --cov=. --cov-report=html --cov-config=.coveragerc'
        archiveArtifacts artifacts: 'htmlcov/**', fingerprint: true
      }
    }

    stage('Lint') {
      steps {
        echo 'Linting...'
        sh 'cd backend'
        sh 'pip install --upgrade pip'
        sh 'pip install -r requirements.txt'
        sh 'flake8 app/ --count --show-source --statistics'
      }
    }

    stage('Build') {
      teps {
        echo 'Building...'
        sh 'git checkout main'
        sh 'pip install --upgrade pip'
        sh 'pip install build'
        sh 'python -m build'
        archiveArtifacts artifacts: 'dist/**', fingerprint: true
      }
    }

    stage('Notification') {
      steps {
        echo 'Sending email...'
        sh '''
          cd scripts/
          chmod 775 *
          ./notification.sh
        '''      
      }
    }
  }
}