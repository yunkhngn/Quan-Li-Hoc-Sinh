from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('Python Guides')
ws.geometry('300x200')
ws.config(bg='#5FB691')

def msg1():
    messagebox.showinfo('information', 'Hi! You got a prompt.')
    messagebox.showerror('error', 'Something went wrong!')
    messagebox.showwarning('warning', 'accept T&C')
    messagebox.askquestion('Ask Question', 'Do you want to continue?')
    messagebox.askokcancel('Ok Cancel', 'Are You sure?')
    messagebox.askyesno('Yes|No', 'Do you want to proceed?')
    messagebox.askretrycancel('retry', 'Failed! want to try again?')

Button(ws, text='Click Me', command=msg1).pack(pady=50)

ws.mainloop()