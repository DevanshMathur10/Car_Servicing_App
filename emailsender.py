import smtplib
import os
import secrets
from email.message import EmailMessage

EMAIL_ADDRESS=os.environ.get('PYMAIL')
EMAIL_PASSWORD=os.environ.get('PYPASS')

p=str(secrets.token_hex(8))
def sendpass(emailget):
    
    body=" "+p
    message=EmailMessage()
    message['Subject']="PASS"
    message['From']=EMAIL_ADDRESS
    message['To']=str(emailget)
    message.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(message)


