import boto3

# AWS S3 Config
BUCKET_NAME = "kaibucket78"

# Initialize S3 client
s3 = boto3.client("s3")

# Get the latest file from S3 bucket
def get_latest_resume():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    if "Contents" in response:
        # Sort files by last modified date (latest first)
        latest_file = sorted(response["Contents"], key=lambda x: x["LastModified"], reverse=True)[0]
        return latest_file["Key"]
    else:
        raise Exception("No files found in S3 bucket!")

# Get the latest resume file
RESUME_FILE = get_latest_resume()

# Save the filename for Jenkins to read
with open("latest_resume.txt", "w") as f:
    f.write(RESUME_FILE)

print(f"Latest resume file: {RESUME_FILE}")
