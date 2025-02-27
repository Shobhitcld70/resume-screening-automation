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

    # Extract data from resume
    extracted_data = process_resume.extract_resume_data(latest_resume)

    if extracted_data:
        print("Updating Google Sheets...")

        # Call the correct function with required arguments
        sheets_utils.send_to_google_sheets(
            extracted_data.get("name", ""),
            extracted_data.get("email", ""),
            extracted_data.get("phone", ""),
            extracted_data.get("sentiment", ""),
            extracted_data.get("summary", "")
        )

        print("Google Sheets updated successfully!")
    else:
        print("No relevant data found in the resume.")

if __name__ == "__main__":
    update_google_sheets()
