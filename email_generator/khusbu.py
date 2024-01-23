from email.message import EmailMessage 
import ssl
import smtplib


email_sender = "codingdbl@gamil.com"
email_password =  "hgjx wikl xgtx gxet"
email_receiver = "nodaso8655@tsderp.com"
subjects = "Hey, baby do you know how much spaces you are userp from my heart so I need to relieve "
body = '''

'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subjects'] = subjects
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtpgmail.com", 465, context= context) as smpt:
    smpt.login(email_sender, email_password)
    smpt.sendmail(email_sender, email_receiver , em.as_string())


# from email.message import EmailMessage 
# import ssl
# import smtplib

# email_sender = "codingdbl@gmail.com"
# email_password = "hgjx wikl xgtx gxet"
# email_receiver = "nodaso8655@tsderp.com"
# subject = "Hey, baby do you know how much space you are usurping from my heart, so I need to relieve it"
# body = '''
# '''

# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject  # Corrected variable name
# em.set_content(body)

# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())
