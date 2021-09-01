# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Demonstrate sending mail via SMTP.
"""


import sys
from email.mime.text import MIMEText

from twisted.python import log
from twisted.mail.smtp import sendmail
from twisted.internet import reactor


def send(message, subject, sender, recipients, host):
    """
    Send email to one or more addresses.
    """
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)

    dfr = sendmail(host.encode('utf-8'), sender.encode('utf-8'), recipients, msg.as_string().encode('utf-8'),port=2500,requireTransportSecurity=False)

    def success(r):
        reactor.stop()

    def error(e):
        print(e)
        reactor.stop()

    dfr.addCallback(success)
    dfr.addErrback(error)

    reactor.run()


if __name__ == "__main__":
    msg = "This is the message body"
    subject = "This is the message subject"

    host = "localhost"
    sender = "sender@example.com"
    recipients = ["hola@localhost"]

    log.startLogging(sys.stdout)
    send(msg, subject, sender, recipients, host)
