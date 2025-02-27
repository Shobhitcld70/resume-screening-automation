import requests

# Google Apps Script Web App URL
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbwx4KyQss6wPb78tWyVXXdyRIje56zE6qgJSChDbRoBB54kTEYYEjMQka34RbrZ9Y9jQg/exec"

def send_to_google_sheets(name, email, phone, sentiment, summary):
    """Send processed resume data to Google Sheets via Apps Script"""
    
    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "sentiment": sentiment,
        "summary": summary
    }

    try:
        response = requests.post(WEB_APP_URL, json=data)
        response.raise_for_status()  # Raises an error for bad responses

        # Check JSON response
        response_data = response.json()
        if response_data.get("status") == "success":
            print("✅ Data sent successfully to Google Sheets!")
        else:
            print("⚠️ Data sent, but check the response:", response_data)

    except requests.exceptions.RequestException as e:
        print("❌ Failed to send data. Error:", e)

# Example usage (for testing)
if __name__ == "__main__":
    send_to_google_sheets("John Doe", "johndoe@example.com", "+1234567890", "Positive", "Experienced Software Engineer.")
