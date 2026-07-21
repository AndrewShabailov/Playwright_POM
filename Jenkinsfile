pipeline {
    agent any

    environment {
        IMAGE_NAME  = 'pw-tests'
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
                    bat "docker run --rm -v %WORKSPACE%\\allure-results:/app/allure-results %IMAGE_NAME% || exit 0"
                }
            }
        }
    }

    post {
        always {
            allure includeProperties: false,
                   jdk: '',
                   results: [[path: 'allure-results']]

            bat "docker image rm %IMAGE_NAME% || exit 0"
        }
    }
}
