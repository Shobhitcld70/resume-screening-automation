pipeline {
    agent any

    stages {
        stage('Setup Python Environment') {
            steps {
                echo '🔧 Setting up Python environment...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Download Resume from S3') {
            steps {
                echo '📥 Downloading latest resume from S3...'
                sh 'aws s3 cp s3://your-resume-bucket/latest_resume.pdf ./resume.pdf'
            }
        }

        stage('Process Resume') {
            steps {
                echo '📝 Extracting text from resume...'
                sh 'python process_resume.py resume.pdf'
            }
        }

        stage('Update Google Sheets') {
            steps {
                echo '📊 Sending extracted data to Google Sheets...'
                sh 'python send_to_sheets.py'
            }
        }
    }

    post {
        success {
            echo '✅ Resume processed and sent successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs for errors.'
        }
    }
}
