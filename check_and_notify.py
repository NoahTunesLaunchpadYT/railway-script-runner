import os
import requests

# Internal Railway URL for your Django server
DJANGO_SERVER_URL = os.getenv("DJANGO_SERVER_URL", "http://django-server.railway.internal/check-and-notify/")

def trigger_check_and_notify():
    try:
        # Send a POST request to the Django server
        response = requests.post(DJANGO_SERVER_URL)
        response.raise_for_status()  # Raise an error for bad status codes

        # Print the response from the server
        print("Response from Django server:", response.json())
    except requests.exceptions.RequestException as e:
        print("Failed to trigger check_and_notify:", e)

if __name__ == "__main__":
    trigger_check_and_notify()