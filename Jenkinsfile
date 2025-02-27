pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    echo 'Setting up Python environment...'
                    bat '"C:\\Users\\umapc\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" -m venv venv'
                    bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Download Resume from S3') {
            steps {
                script {
                    echo 'Downloading resume from S3...'
                    bat 'aws s3 cp s3://kaibucket78/resume.pdf .'
                }
            }
        }

        stage('Process Resume') {
            steps {
                script {
                    echo 'Processing resume...'
                    bat '.\\venv\\Scripts\\python.exe process_resume.py resume.pdf'
                }
            }
        }

        stage('Update Google Sheets') {
            steps {
                script {
                    echo 'Updating Google Sheets...'
                    bat '.\\venv\\Scripts\\python.exe update_sheets.py'
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
