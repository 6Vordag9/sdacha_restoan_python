import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendMail(email):
     smtpEmail = "udrive00@mail.ru"
     smtpObj = smtplib.SMTP("smtp.mail.ru", 587)
     smtpObj.starttls()
     smtpObj.login(smtpEmail, "zcyWmDRBPMLPRr45Hsrm")
     code = random.randint(100000, 999999)
     smtpObj.sendmail(smtpEmail, email, f"Это твой код для регистрация напиши его и у тебя не будет проблем с ней: {code}")
     smtpObj.quit()
     return code