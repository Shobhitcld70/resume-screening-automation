import boto3

# AWS S3 Config
BUCKET_NAME = "kaibucket78"
LOCAL_PROCESSED_FILE = "output/processed_resume.pdf"
S3_PROCESSED_FILE = "processed_resumes/processed_resume.pdf"

# Initialize S3 client
s3 = boto3.client("s3")

# Upload processed file to S3
s3.upload_file(LOCAL_PROCESSED_FILE, BUCKET_NAME, S3_PROCESSED_FILE)

print(f"✅ Processed resume uploaded to S3: s3://{BUCKET_NAME}/{S3_PROCESSED_FILE}")
