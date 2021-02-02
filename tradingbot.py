import smtplib
## TODO Turn these into local environment variables
LOCAL_PASS = 'dqjneidxxetuqrrh'
LOCAL_EMAIL = "notifbot69420@gmail.com"

class emailHandler:
    def sendEmail(self, email, body):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(LOCAL_EMAIL, LOCAL_PASS)
            subject = 'TradeBot'
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail(email, email, msg)