import smtplib
## TODO Turn these into local environment variables
LOCAL_PASS = ""
LOCAL_EMAIL = ""

class emailHandler:
    def sendEmail(self, email, body):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(LOCAL_EMAIL, LOCAL_PASS)
            subject = 'TradeBot Update'
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail(email, email, msg)


class tradingBot:
    def __init__(self, emailHandler):
        self.emailHandler = emailHandler
        self.email = 'grumblyguy@gmail.com'

    def sendEmail(self, body):
        self.emailHandler.sendEmail(self.email, body)
     

bot = tradingBot(emailHandler())
