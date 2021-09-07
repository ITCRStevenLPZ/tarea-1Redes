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
	print(from_entry.get()) 
	print(to_entry.get().split(sep=', '))
	print(subject_entry.get()) 
	print(retrieve_body())
		
submit = Button(root, text='Send Mail' , command = buttonClick, width=20,bg="black",fg='white').place(x=180,y=560)



root.mainloop()


