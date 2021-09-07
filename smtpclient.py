import sys
from email.mime.text import MIMEText

from twisted.python import log
from twisted.mail.smtp import sendmail
from twisted.internet import reactor
from twisted.python.usage import Options, UsageError

def send(message, subject, sender, recipients, host, port):
    """
    Send email to one or more addresses.
    """
    
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    print(msg)

    dfr = sendmail(host, sender, recipients, msg,port=int(port))

    def success(r):
        reactor.stop()

    def error(e):
        print(e)
        reactor.stop()

    dfr.addCallback(success)
    dfr.addErrback(error)

    reactor.run()

'''class MailClientOptions(Options):
    synopsis = "smptclient.py [options]"

    optParameters = [
        (
            "serverhost",
            "h",
            None,
            "Sytax: hostname:serverport",
        ),
        (
            "csv",
            "c",
            None,
            "The path of the CSV file containing destination and source addresses",
        ),
        ("message", "m", None, "The path of the MSG file")
    ]

    def postOptions(self):
        """
        Parse integer parameters, open the message file, and make sure all
        required parameters have been specified.
        """
        if self["serverhost"] is None:
            raise UsageError("Must specify the server name and the port number after : char (port 25 not allowed) with -h or --serverhost")
        try:
            parameters = self["serverhost"].split(sep=":")
            parameters [1] = int(self["serverhost"].split(sep=":")[1])
        except ValueError:
            raise UsageError("Port number must be included. Ex: localhost:2500 ")

        if self["csv"] is None:
            raise UsageError("Must specify a csv path with -c or --csv")
        try:
            testing = open(self["message"],'r')
        except Exception as e:
            raise UsageError(e)

        if self["message"] is None:
            raise UsageError("Must specify a message path with -m or --message")
        try:
            testing = open(self["message"],'r')
        except Exception as e:
            raise UsageError(e)'''

def GetRecipients(addARR):
    awsr = []
    for i in addARR:
        awsr.append(i[0])
    return awsr



'''def main(args=None):

    import sys
    o = MailClientOptions()
    try:
        o.parseOptions(args)
    except UsageError as e:
        raise SystemExit(e)

    msgList = []
    import csv

    with open("msg.csv", 'r') as msgfile:
        spamreader = csv.reader(msgfile, delimiter='\n', quotechar='|')
        for row in spamreader:
            msgList.append(row)

    addresses = []

    with open(o["csv"], 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
        for row in spamreader:
            new = row[0].split(sep=',')
            addresses.append(new)


    subject = str(msgList[0][0])

    body = msgList[1:]
    msg = ''.join(''.join(elems) for elems in body)
    host = o["serverhost"].split(sep=":")[0]
    port = int(o["serverhost"].split(sep=":")[1])
    sender = "test@example.com"
    recipients = GetRecipients(addresses)
    log.startLogging(sys.stdout)
    send(msg, subject, sender, recipients, host, port)





if __name__ == "__main__":
    main(sys.argv[1:])'''

from tkinter import *

root = Tk()
        
root.configure(background='white')

root.geometry("500x600")

root.title('Send Mail')

label_0 =Label(root,text="Ronald's SMTP Client", width=40,font=("bold",20))
label_0.place(x=0,y=60)

label_1 =Label(root,text="From", width=10,font=("bold",10))
label_1.place(x=0,y=130)

from_entry=Entry(root, width=50)
from_entry.place(x=100,y=130)

label_2 =Label(root,text="To", width=10,font=("bold",10))
label_2.place(x=0,y=180)

to_entry=Entry(root, width=50)
to_entry.place(x=100,y=180)

label_3 =Label(root,text="Subject", width=10,font=("bold",10))
label_3.place(x=0,y=230)

subject_entry=Entry(root, width=50)
subject_entry.place(x=100,y=230)

label_4 =Label(root,text="Body", width=10,font=("bold",10))
label_4.place(x=0,y=280)

body_entry=Text(root, width=50, height=20)
body_entry.place(x=100,y=280)

def retrieve_body():
    input = body_entry.get("1.0",END)
    return input

def buttonClick():
    subject = subject_entry.get()
    msg = retrieve_body()
    host = "localhost"
    port = 2500
    sender = from_entry.get()
    recipients = to_entry.get().split(sep=', ')
    log.startLogging(sys.stdout)
    send(msg, subject, sender, recipients, host, port)


submit = Button(root, text='Send Mail' , command = buttonClick, width=20,bg="black",fg='white').place(x=180,y=560)


root.mainloop()