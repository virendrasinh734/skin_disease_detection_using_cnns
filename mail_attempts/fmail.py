from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration for Flask-Mail (replace with your own settings)
app.config['MAIL_SERVER'] = 'smtp.rediffmailpro.com'  # Your SMTP server
app.config['MAIL_PORT'] = 465  # SMTP port (587 for TLS)
app.config['MAIL_USERNAME'] = 'innomindscontacts@rediffmail.com'
app.config['MAIL_PASSWORD'] = 'q7z2qwfhx344ssogc4'
app.config['MAIL_USE_TLS'] = False  # Use TLS (or False for SSL)
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'innomindscontacts@rediffmail.com'  # Default sender

mail = Mail(app)

@app.route('/')
def index():
    recipient_email = "virendrasinhkhuman@gmail.com"
    subject = 'Hello!'
    message = 'This is a test email.'

    msg = Message(subject=subject, recipients=[recipient_email])
    msg.body = message

    try:
        mail.send(msg)
        return 'Email sent successfully.'
    except Exception as e:
        return f'Email could not be sent. Error: {str(e)}'

@app.route('/send_email')
def send_email():
    recipient_email = "virendrasinhkhuman@gmail.com"
    subject = 'Hello!'
    message = 'This is a test email.'

    msg = Message(subject=subject, recipients=[recipient_email])
    msg.body = message

    try:
        mail.send(msg)
        return 'Email sent successfully.'
    except Exception as e:
        return f'Email could not be sent. Error: {str(e)}'

if __name__ == '__main__':
    app.run()
