from email.message import EmailMessage
from pwdemail import pwd
import ssl
import smtplib

email_sender='mercyjoshan@gmail.com'
email_pwd=pwd
email_receiver='patowo7221@bongcs.com'
subject='Greetings'
body="""
Hey, how you doing?
"""

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body) 

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host:'smtp.gmail.com', 465:context=context) as smtp:
    smtp.login(email_sender, email_pwd)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


