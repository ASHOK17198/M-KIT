import pandas as da
import smtplib
from .tool import config as ca
from .tool import pagan as data

e = da.read_excel("Email.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(ca.SenderAddress, ca.password)

body = "Subject: {}\n\n{}".format(data.subject,data.msg)
for email in emails:
    print("sending to"+email)
    server.sendmail(SenderAddress, email, body)
    
    print("sending success")   
server.quit()


  
  	