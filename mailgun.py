import os
import requests

# Load Mailgun API credentials from environment variables
MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN')

def send_email(user_email, information):
    mailgun_url = f'https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages'
    mailgun_data = {
        'from': 'your_email@example.com',
        'to': user_email,
        'subject': 'Skin Disease Prediction Information',
        'text': f"Here is the information you requested: {information}"
    }

    response = requests.post(
        mailgun_url,
        auth=('api', MAILGUN_API_KEY),
        data=mailgun_data
    )

    if response.status_code == 200:
        print("Email sent successfully")
    else:
        print("Error sending email:", response.text)

