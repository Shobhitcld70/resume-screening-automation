import sheets_utils
import process_resume

def update_google_sheets():
    """
    Extracts relevant information from the latest resume and updates Google Sheets.
    """
    try:
        print("📄 Fetching latest resume...")

        # Get the latest resume file from S3
        latest_resume = process_resume.get_latest_resume()

        if not latest_resume:
            print("⚠️ No latest resume found in S3.")
            return

        print(f"📂 Processing resume: {latest_resume}")

        # Extract data from resume
        extracted_data = process_resume.extract_resume_data(latest_resume)

        if not extracted_data:
            print("⚠️ No relevant data found in the resume.")
            return

        print("🔍 Extracted Data:", extracted_data)  # Debugging log

        # Call the correct function with required arguments
        response = sheets_utils.send_to_google_sheets(
            extracted_data.get("name", "N/A"),
            extracted_data.get("email", "N/A"),
            extracted_data.get("phone", "N/A"),
            extracted_data.get("sentiment", "N/A"),
            extracted_data.get("summary", "N/A")
        )

        print("🔄 Google Sheets API Response:", response)  # Debugging log

        if response and response.get("status") == "success":
            print("✅ Google Sheets updated successfully!")
        else:
            print("❌ Failed to update Google Sheets. Response:", response)

    except Exception as e:
        print("❌ Error updating Google Sheets:", str(e))

if __name__ == "__main__":
    update_google_sheets()
