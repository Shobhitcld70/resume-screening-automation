import sheets_utils
import process_resume

def update_google_sheets():
    """
    Extracts relevant information from the latest resume and updates Google Sheets.
    """
    print("Fetching latest resume...")
    
    # Get the latest resume file from S3
    latest_resume = process_resume.get_latest_resume()
    
    print(f"Processing resume: {latest_resume}")
    
    # Extract data from resume (modify based on actual extraction logic)
    extracted_data = process_resume.extract_resume_data(latest_resume)

    if extracted_data:
        print("Updating Google Sheets...")
        sheets_utils.update_sheets(extracted_data)
        print("Google Sheets updated successfully!")
    else:
        print("No relevant data found in the resume.")

if __name__ == "__main__":
    update_google_sheets()
