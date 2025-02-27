pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = 'AKIASVLKCCI5HSX24XGK'
        AWS_SECRET_ACCESS_KEY = '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'
        AWS_DEFAULT_REGION = 'us-east-1'
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
                    echo 'Setting up Python virtual environment...'
                    bat '"C:\\Users\\umapc\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" -m venv venv'
                    
                    // Correct way to upgrade pip
                    bat '.\\venv\\Scripts\\python.exe -m pip install --upgrade pip'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing required Python dependencies...'
                    bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
                    
                    // Ensure pdfminer.six and pdfplumber are installed
                    bat '.\\venv\\Scripts\\activate && pip install pdfminer.six pdfplumber'
                }
            }
        }

        stage('Verify Installations') {
            steps {
                script {
                    echo 'Verifying installed dependencies...'
                    bat '.\\venv\\Scripts\\activate && python -m pip list'
                }
            }
        }

        stage('Get Latest Resume Filename') {
            steps {
                script {
                    echo 'Fetching latest resume filename from S3...'
                    bat '.\\venv\\Scripts\\activate && python process_resume.py'
                }
            }
        }

        stage('Download Latest Resume from S3') {
            steps {
                script {
                    echo 'Downloading latest resume from S3...'
                    def latestResume = readFile('latest_resume.txt').trim()
                    echo "Downloading: ${latestResume}"
                    bat "aws s3 cp \"s3://kaibucket78/${latestResume}\" ."
                }
            }
        }

        stage('Process Resume') {
            steps {
                script {
                    echo 'Processing resume with pdfminer and pdfplumber...'
                    bat '.\\venv\\Scripts\\activate && python process_resume.py latest_resume.txt'
                }
            }
        }

        stage('Update Google Sheets') {
            steps {
                script {
                    echo 'Updating Google Sheets...'
                    bat '.\\venv\\Scripts\\activate && python update_sheets.py'
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
