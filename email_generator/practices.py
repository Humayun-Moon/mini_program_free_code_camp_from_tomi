from email.message import EmailMessage
import ssl
import smtplib

email_sender = ""
email_password = ""
email_receiver = ""
subjects = "Please contact me as soon as possible we have some appointment tonight and they would pay more dimand"
body ='''
Dear, Khusbu hope Allah kept you happy Do you know what's going to few day I have passed often I feel you and I lose my mind inside your intution so I must needed now your apporach otherwise I'm going to be mad 
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subjects'] = subjects

em.set_content(body) 

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp@gmail.com', 556, context= context) as smpt:
    smpt.login(email_sender, email_password)
    smpt.sendmail(email_sender, email_receiver, em.as_string())