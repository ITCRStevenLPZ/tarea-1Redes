from twisted.mail import smtp, maildir
from zope.interface import implementer
from twisted.python.usage import Options, UsageError
from twisted.internet import protocol, reactor, defer
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
from OpenSSL.crypto import load_privatekey, load_certificate, FILETYPE_PEM

import os
import sys


@implementer(smtp.IMessage)
class MaildirMessageWriter(object):

    def __init__(self, userDir):
        if not os.path.exists(userDir): os.mkdir(userDir)
        inboxDir = os.path.join(userDir, 'Inbox')
        self.mailbox = maildir.MaildirMailbox(inboxDir)
        self.lines = []

        print ("Creating an Inbox Directory in: %s" %inboxDir)

    def lineReceived(self, line):
        if isinstance(line, str):
            self.lines.append(line)
        else:
            self.lines.append(line.decode('utf8', 'strict'))
        

    def eomReceived(self):
        # message is complete, store it
        print ("Message data complete.")
        self.lines.append('') # add a trailing newline
        messageData = ''.join(self.lines)
        messageData = str.encode(messageData)
        type(messageData)
        return self.mailbox.appendMessage(messageData)



    def connectionLost(self):
        print ("Connection lost unexpectedly!")
        # unexpected loss of connection; don't save



@implementer(smtp.IMessageDelivery)
class LocalDelivery(object):
    

    def __init__(self, baseDir, validDomains):

        if not os.path.isdir(baseDir):

            raise ValueError

        self.baseDir = baseDir


        encodedDomains = []
        for dom in validDomains:
            encodedDomains.append(dom.encode('utf-8'))

        self.validDomains = encodedDomains



    def receivedHeader(self, helo, origin, recipients):

        myHostname, clientIP = helo

        headerValue = "by %s from %s with ESMTP ; %s" % (myHostname, clientIP, smtp.rfc822date( ))

        # email.Header.Header used for automatic wrapping of long lines

        return ("Received: %s" % headerValue)



    def validateTo(self, user):

        if not user.dest.domain in self.validDomains:
            print ("Bad recipients: %s" %user.dest.domain)
            raise smtp.SMTPBadRcpt(user)

        print ("Accepting mail for %s..." % user.dest)

        return lambda: MaildirMessageWriter(

        self._getAddressDir(str(user.dest)))



    def _getAddressDir(self, address):

        return os.path.join(self.baseDir, "%s" % address)



    def validateFrom(self, helo, originAddress):

        # accept mail from anywhere. To reject an address, raise

        # smtp.SMTPBadSender here.

        return originAddress

class MailServerOptions(Options):
    synopsis = "smtpserver.py [options]"

    optParameters = [
        (
            "domains",
            "d",
            None,
            "The domains accpted by the server separated by comma.",
        ),
        (
            "storage",
            "s",
            None,
            "The path of the mail-storage directory.",
        ),
        ("port", "p", None, "The port of the server. Port 25 is not allowed.")
    ]

    def postOptions(self):
        """
        Parse integer parameters, open the message file, and make sure all
        required parameters have been specified.
        """
        if self["port"] is None:
            raise UsageError("Must specify a port number (port 25 not allowed) with -p or --port")
        try:
            self["port"] = int(self["port"])
        except ValueError:
            raise UsageError("Port argument must be a number.")
        if self["storage"] is None:
            raise UsageError("Must specify a mail-storage path with -s or --storage")
        if self["domains"] is None:
            raise UsageError("Must specify the server accepted domains sepated by a comma with -d or --domains")



class SMTPServer(protocol.ServerFactory):
            


    def __init__(self, baseDir, validDomains, contextFactory):

        self.baseDir = baseDir

        self.validDomains = validDomains

        self.contextFactory = contextFactory

    def lineReceived(self, line):
        print ("received: " + line)



    def buildProtocol(self, addr):

         delivery = LocalDelivery(self.baseDir, self.validDomains)

         smtpProtocol = smtp.SMTP(delivery)

         #esmtpProtocol = smtp.ESMTP(contextFactory = self.contextFactory)

         #esmtpProtocol.SMTP = smtpProtocol


         return smtpProtocol

def main(args=None):

    import sys
    o = MailServerOptions()
    try:
        o.parseOptions(args)
    except UsageError as e:
        raise SystemExit(e)

    #mailboxDir = sys.argv[1]

    domains = o["domains"].split(",")

    from twisted.internet import ssl

    certFile = open("keys/example.crt","r")
    keyFile = open("keys/example.key","r")
    pKeyData = keyFile.read()
    certData = certFile.read()
    cert = load_certificate(FILETYPE_PEM, certData)
    pKey = load_privatekey(FILETYPE_PEM, pKeyData)
    sslCtxFactory = ssl.CertificateOptions(privateKey=pKey, certificate=cert)

    factory = SMTPServer(o["storage"],domains,sslCtxFactory)

    reactor.listenTCP(2500, factory)


    reactor.run()

if __name__ == "__main__":
    main(sys.argv[1:])
