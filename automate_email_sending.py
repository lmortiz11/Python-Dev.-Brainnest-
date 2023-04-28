''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

from email.message import EmailMessage
import smtplib, ssl

from os.path import basename
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import schedule
import time

import logging


def send_email():
    
    logging.basicConfig(filename='email_send.log',level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    email_sender = "pythonemail.project2023@gmail.com"  # Enter email address from where the messages will be send 
    email_receiver = ["lina.ortizparra96@gmail.com" ,"arielortizb@gmail.com"] # Enter list of email adrress
    password ="krngelroardtylxk"


    subject= 'Daily report'
    body_text="""
    Attached you'll find the daily report.
    """

    msg=MIMEMultipart()
    msg['From']=email_sender
    msg['Subject']=subject

    body=MIMEText(body_text, 'plain')
    msg.attach(body)

    context = ssl.create_default_context()

    #open the file name of the report you'll send
    filename = "report.txt" 

    # Open the file
    with open(filename, "r") as f:
        
        attachment = MIMEApplication(f.read(), Name=basename(filename))
        attachment['Content-Disposition']='attachment; filename"{}"'.format(basename(filename))
    
    msg.attach(attachment)
    
    try:
        for i in range (len(email_receiver)):
            msg['To']=email_receiver[i]
            name_email= email_receiver[i]
            
    
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            
                server.login(email_sender, password)
                server.sendmail(email_sender, email_receiver, msg.as_string())
            
            logging.info( '{} successfully sent email'.format(name_email))
            
    except SMTPException:
        
        logging.warning("Error: unable to send email")
        
        
#schedule send
       

schedule.every().day.at("8:00").do(send_email,'It is 8:00')

while True:
    schedule.run_pending()
    time.sleep(60)
