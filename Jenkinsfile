pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = 'AKIASVLKCCI5HSX24XGK'
        AWS_SECRET_ACCESS_KEY = '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'
        AWS_REGION = 'us-east-1'  // Change this if needed
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
                }
            }
        }

        stage('Configure AWS Credentials') {
            steps {
                script {
                    echo 'Setting up AWS credentials...'
                    bat '''
                    mkdir %USERPROFILE%\\.aws 2>nul
                    echo [default] > %USERPROFILE%\\.aws\\credentials
                    echo aws_access_key_id=%AWS_ACCESS_KEY_ID% >> %USERPROFILE%\\.aws\\credentials
                    echo aws_secret_access_key=%AWS_SECRET_ACCESS_KEY% >> %USERPROFILE%\\.aws\\credentials

                    echo [default] > %USERPROFILE%\\.aws\\config
                    echo region=%AWS_REGION% >> %USERPROFILE%\\.aws\\config
                    '''
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
