from email.message import EmailMessage 
from app2 import password 
import ssl
import smtplib

email_sender = "codingdbl@gmail.com"
email_password = password 
email_receiver = "johajax689@tanlanav.com"
sub = "Don't forget to come on the right time"
body = """
Hey Dear, We may come today at my home 
""" 

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = sub  # Corrected attribute name
em.set_content(body) 

context = ssl.create_default_context()

# Corrected SMTP server address and port
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password) 
    smtp.sendmail(email_sender, email_receiver, em.as_string())
