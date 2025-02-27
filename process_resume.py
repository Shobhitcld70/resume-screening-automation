import boto3
import pdfplumber

# AWS S3 Config
BUCKET_NAME = "kaibucket78"
s3 = boto3.client("s3")

# Get the latest file from S3 bucket
def get_latest_resume():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    if "Contents" in response:
        latest_file = sorted(response["Contents"], key=lambda x: x["LastModified"], reverse=True)[0]
        return latest_file["Key"]
    else:
        raise Exception("No files found in S3 bucket!")

# Extract text from resume
def extract_resume_data(resume_file):
    print(f"Extracting data from {resume_file}...")
    
    # Download the file from S3
    s3.download_file(BUCKET_NAME, resume_file, resume_file)

    # Open PDF and extract text
    with pdfplumber.open(resume_file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    
    return {"resume_text": text}  # Modify as needed to extract structured data
