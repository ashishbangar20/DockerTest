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
                    bat """
                    docker run --rm ^
                        -v %%CD%%:/app ^
                        -w /app ^
                        ${IMAGE_NAME} ^
                        pytest --html=${REPORT_DIR}/report.html --self-contained-html
                    """
                }
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: "${REPORT_DIR}/**", allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            cleanWs()
        }
        success {
            echo '✅ Test pipeline completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
