import requests
import sys

# Fix for Unicode issues in Windows
sys.stdout.reconfigure(encoding='utf-8')

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzOb6QSNKUskCL_8zayo8H7b3ObltM5kXaHKA4PVwMl7QArOEZ1YMW2T3JZNUtrFYSUfA/exec"

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
        
        # Debugging: Print raw response
        print("🔄 Response Status Code:", response.status_code)
        print("📄 Response Text:", response.text)  

        response.raise_for_status()  # Raises an error for bad responses

        response_data = response.json()
        if response_data.get("status") == "success":
            print("✅ Data sent successfully to Google Sheets!")
        else:
            print("⚠️ Data sent, but check the response:", response_data)

    except requests.exceptions.JSONDecodeError:
        print("⚠️ Error: Response is not valid JSON. Check Web App URL or deployment.")
    except requests.exceptions.RequestException as e:
        print("Failed to send data. Error:", e)
