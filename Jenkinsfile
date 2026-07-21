pipeline {
    agent any

    environment {
        IMAGE_NAME  = 'PW-tests'
        PROJECT_DIR = '.'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker image') {
            steps {
                dir("${PROJECT_DIR}") {
                    bat "docker build -t %IMAGE_NAME% ."
                }
            }
        }

        stage('Run tests') {
            steps {
                dir("${PROJECT_DIR}") {
                    bat "docker run --rm %IMAGE_NAME%"
                }
            }
        }
    }

    post {
        always {
            bat "docker image rm %IMAGE_NAME% || exit 0"
        }
    }
}