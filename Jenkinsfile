pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest tests.py -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Payroll Application...'
            }
        }
    }
}
