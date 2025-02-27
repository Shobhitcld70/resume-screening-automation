import boto3

textract = boto3.client("textract")
comprehend = boto3.client("comprehend")

def extract_text_from_s3(bucket_name, file_name):
    response = textract.analyze_document(
        Document={"S3Object": {"Bucket": bucket_name, "Name": file_name}},
        FeatureTypes=["TABLES", "FORMS"]
    )

    extracted_text = ""
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            extracted_text += item["Text"] + "\n"

    return extracted_text

def analyze_text_with_comprehend(text):
    response = comprehend.detect_sentiment(Text=text, LanguageCode="en")
    return response
