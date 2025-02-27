pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = 'AKIASVLKCCI5HSX24XGK'
        AWS_SECRET_ACCESS_KEY = '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'
        AWS_DEFAULT_REGION = 'us-east-1'  // Change if needed
        PYTHONPATH = "C:\\Users\\umapc\\Downloads\\pdfplumber-0.11.5;C:\\Users\\umapc\\Downloads\\pdfplumber-0.11.5\\pdfminer"
    }

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
                    bat '.\\venv\\Scripts\\activate && pip install pdfplumber pdfminer.six'
                }
            }
        }

        stage('Verify Dependencies') {
            steps {
                script {
                    echo 'Verifying installed dependencies...'
                    bat '.\\venv\\Scripts\\python.exe -m pip list'
                }
            }
        }

        stage('Get Latest Resume Filename') {
            steps {
                script {
                    echo 'Getting latest resume filename from S3...'
                    bat '.\\venv\\Scripts\\python.exe process_resume.py'
                }
            }
        }

        stage('Download Latest Resume from S3') {
            steps {
                script {
                    echo 'Reading the latest resume filename...'
                    def latestResume = readFile('latest_resume.txt').trim()
                    echo "Downloading: ${latestResume}"
                    bat "aws s3 cp \"s3://kaibucket78/${latestResume}\" ."
                }
            }
        }

        stage('Process Resume') {
            steps {
                script {
                    echo 'Processing resume...'
                    bat '.\\venv\\Scripts\\python.exe process_resume.py latest_resume.txt'
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
