import math
import smtplib
import ssl
import random

def format_message(content: str, sender: str):
    subject = "Verification Code"
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (
        content,
        sender,
        subject,
        content,
    )
    return email_text


class EmailService:
    sender_email: str
    sender_password: str
    context: object


    def __init__(self, sender_email: str, sender_password: str):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.context = ssl.create_default_context()
        self.port = 587  # For starttls
        self.smtp_server = "smtp.gmail.com"


    def sendVerificationCode(self,receiver_email, receiver_name,code):
        message = f"""\
    Object: Verification code

        Hello {receiver_name} This is your verification code: {code} """
        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, receiver_email, message)