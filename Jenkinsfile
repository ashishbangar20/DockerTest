pipeline {
    agent any

    environment {
        IMAGE_NAME = "pytest-framework"
        REPORT_DIR = "reports"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/ashishbangar20/DockerTest.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("${IMAGE_NAME}").inside {
                        sh 'pytest --html=reports/report.html --self-contained-html'
                    }
                }
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: "${REPORT_DIR}/**", allowEmptyArchive: true
                junit '**/reports/*.xml' // optional, if using JUnit-style reporting
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            cleanWs()
        }
        success {
            echo 'Test pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
