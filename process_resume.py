import boto3
import pdfplumber
import re

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
    print(f"📄 Extracting data from {resume_file}...")

    # Download the file from S3
    s3.download_file(BUCKET_NAME, resume_file, resume_file)

    # Open PDF and extract text
    with pdfplumber.open(resume_file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

    print("📝 Extracted Text:", text[:500])  # Debug: Print first 500 characters

    # Extract name (assumes first non-empty line is the name)
    name = text.split("\n")[0] if text else "N/A"

    # Extract email using regex
    email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    email = email_match.group(0) if email_match else "N/A"

    # Extract phone number using regex
    phone_match = re.search(r"\+?\d{1,3}[\s-]?\d{10}", text)  # Matches international & local numbers
    phone = phone_match.group(0) if phone_match else "N/A"

    # Placeholder for sentiment analysis (modify based on NLP model)
    sentiment = "Neutral"

    # Summary (first 2 lines as summary)
    summary = " ".join(text.split("\n")[:2]) if text else "N/A"

    extracted_data = {
        "name": name.strip(),
        "email": email.strip(),
        "phone": phone.strip(),
        "sentiment": sentiment,
        "summary": summary.strip()
    }

    print("🔍 Extracted Data:", extracted_data)  # Debug log

    return extracted_data  # Now returns structured data

