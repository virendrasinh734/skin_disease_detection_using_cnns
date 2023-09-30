import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Rediffmail SMTP server details
smtp_server = 'smtp.rediffmail.com'
smtp_port = 25  # Use port 25 for non-encrypted SMTP
sender_email = 'innomindscontacts@rediffmail.com'
sender_password = 'Innominds@123'

def send_email(recipient_email, subject, message):
    max_retries = 3
    retry_delay = 5  # seconds

    for attempt in range(max_retries):
        try:
            # Create an SMTP connection without encryption
            context = smtplib.SMTP(smtp_server, smtp_port)

            # Login to your Rediffmail account
            context.login(sender_email, sender_password)

            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Attach the message
            msg.attach(MIMEText(message, 'plain'))

            # Send the email
            context.sendmail(sender_email, recipient_email, msg.as_string())

            # Close the connection
            context.quit()

            return True
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
    
    return False

# Example usage:
recipient_email = 'virendrasinhkhuman@gmail.com'
subject = 'Hello!'
message = 'This is a test email.'

# Call the send_email function to send the email
if send_email(recipient_email, subject, message):
    print('Email sent successfully.')
else:
    print('Email could not be sent after multiple attempts.')
