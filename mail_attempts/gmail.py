import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail SMTP server details
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'innomindscontacts@gmail.com'
sender_password = 'InnoMindsContacts'

def send_email(recipient_email, subject, message):
    try:
        # Create a secure SSL context
        context = smtplib.SMTP(smtp_server, smtp_port)
        context.starttls()

        # Login to your Gmail account
        context.login(sender_email, sender_password)

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        context.sendmail(sender_email, recipient_email, msg.as_string())

        # Close the connection
        context.quit()

        return True
    except Exception as e:
        print(str(e))
        return False

# Example usage:
recipient_email = 'user@example.com'
subject = 'Hello!'
message = 'This is a test email.'
send_email(recipient_email, subject, message)
