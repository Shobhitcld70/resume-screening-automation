pipeline {
    agent any

    environment {
        S3_BUCKET = "kaibucket78"  // 🔹 Your S3 bucket name
        AWS_REGION = "us-east-1"   // 🔹 Your AWS region
        WEB_APP_URL = "https://script.google.com/macros/s/AKfycbwx4KyQss6wPb78tWyVXXdyRIje56zE6qgJSChDbRoBB54kTEYYEjMQka34RbrZ9Y9jQg/exec"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Shobhitcld70/resume-screening-automation.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Download Latest Resume from S3') {
            steps {
                script {
                    sh """
                        aws s3 cp s3://$S3_BUCKET/resumes/ latest_resume.pdf
                    """
                }
            }
        }

        stage('Process Resume') {
            steps {
                sh 'python3 process_resume.py latest_resume.pdf'
            }
        }

        stage('Update Google Sheets') {
            steps {
                sh 'python3 sheets_util.py'
            }
        }
    }

    post {
        success {
            echo "✅ Resume processing and Google Sheets update completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check logs for errors."
        }
    }
}
