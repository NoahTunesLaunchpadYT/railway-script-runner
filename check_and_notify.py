import os
import requests

# Internal Railway URL for your Django server
RAILWAY_PRIVATE_DOMAIN = os.getenv("RAILWAY_PRIVATE_DOMAIN", "django-server.railway.internal")
PORT = os.getenv("PORT", "8000")  # Default to 8000 if PORT is not set
DJANGO_SERVER_URL = f"http://{RAILWAY_PRIVATE_DOMAIN}:{PORT}/unread-message-notifications/"

def trigger_unread_message_notifications():
    try:
        # Send a POST request to the Django server
        response = requests.post(DJANGO_SERVER_URL)
        response.raise_for_status()  # Raise an error for bad status codes

        # Print the response from the server
        print("Response from Django server:", response.json())
    except requests.exceptions.RequestException as e:
        print("Failed to trigger unread_message_notifications:", e)

if __name__ == "__main__":
    trigger_unread_message_notifications()
