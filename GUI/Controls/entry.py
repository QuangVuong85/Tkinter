from tkinter import *
from tkinter import messagebox

def messageLogin():
    if entryAccount.get() == "":
        lblAccountWarnning = Label(lblFrame, text='*', fg="red")
        lblAccountWarnning.grid(row=0, column=2)
    
    
    if entryPassword.get() == "":
        entryPasswordWarnning = Label(lblFrame, text='*', fg="red")
        entryPasswordWarnning.grid(row=1, column=2)
    

    if entryPassword.get() == "" and entryAccount.get() == "":
        lblAccountWarnning = Label(lblFrame, text='*', fg="red")
        lblAccountWarnning.grid(row=0, column=2)
        entryPasswordWarnning = Label(lblFrame, text='*', fg="red")
        entryPasswordWarnning.grid(row=1, column=2)

master = Tk()

lblFrame = LabelFrame(master)
lblFrame.pack()

lblAccount = Label(lblFrame, text='Account')
lblAccount.grid(row=0, column=0)

entryAccount = Entry(lblFrame)
entryAccount.grid(row=0, column=1)

lblPassword = Label(lblFrame, text='Password')
lblPassword.grid(row=1, column=0)

entryPassword = Entry(lblFrame)
entryPassword.grid(row=1, column=1)

btnLogin = Button(lblFrame, text='Login', command=messageLogin)
btnLogin.grid(row=2, column=1, sticky=W)

btnExit = Button(lblFrame, text='Exit', command=master.destroy)
btnExit.grid(row=2, column=1, sticky=E)

master.mainloop()