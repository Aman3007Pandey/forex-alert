import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage

load_dotenv()
sender_gmail=os.getenv("sender_gmail")
sender_app_password=os.getenv("sender_app_password")
receiver_gmail=os.getenv("receiver_gmail")

def send_gmail(subject,body):
    content=EmailMessage()
    content['Subject']=subject
    content["From"]=sender_gmail
    content["To"]=receiver_gmail
    content.set_content(body)


    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp :
            smtp.login(sender_gmail,sender_app_password)
            smtp.send_message(content)
            print("Emailed Send Successfully :)")
    except:
        print("Failed to send Email :(")        

