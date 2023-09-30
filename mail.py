import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(user_email, information):
    smtp_server = 'smtp.mailgun.org'
    smtp_port = 587  
    
    # Your Yahoo Mail email address and password
    smtp_username = 'postmaster@sandbox61a9bae4643d4f44bd7724c038dfe166.mailgun.org'
    smtp_password = '182dda62d41c4e53e87009ec1e3cb689-db137ccd-9d590c13'

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = user_email
    msg['Subject'] = 'Skin Disease Prediction Information'

    # Add the information to the email body
    body = f"Here is the information you requested:\n {information}\n\nThank you for using our service!\nStay Safe!\n\Regards Team Inno_Minds"
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create an SMTP connection with TLS (STARTTLS)
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to your Yahoo Mail account
        server.login(smtp_username, smtp_password)
        print("logged in")
        # Send the email
        server.sendmail(smtp_username, user_email, msg.as_string())

        # Close the SMTP server
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", str(e))

# Example usage:
# send_email('virendrasinhkhuman@gmail.com', 'This is the information you requested')
