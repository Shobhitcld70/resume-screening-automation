pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'  // Set your AWS region
        S3_BUCKET = 'kaibucket78'  // Corrected bucket name
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    echo 'Cloning the repository...'
                    checkout scm
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    echo 'Setting up Python environment...'
                    bat 'python -m venv venv'
                    bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Download Resume from S3') {
            steps {
                script {
                    echo 'Downloading resume from S3...'
                    bat "aws s3 cp s3://kaibucket78/resume.pdf ."
                }
            }
        }

        stage('Process Resume') {
            steps {
                script {
                    echo 'Processing the resume...'
                    bat '.\\venv\\Scripts\\activate && python process_resume.py'
                }
            }
        }

        stage('Update Google Sheets') {
            steps {
                script {
                    echo 'Updating Google Sheets...'
                    bat '.\\venv\\Scripts\\activate && python update_google_sheets.py'
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    echo 'Cleaning up temporary files...'
                    bat 'deactivate'
                    bat 'rmdir /s /q venv'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
