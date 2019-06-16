from tkinter import *

master = Tk()

### Messge: display multiline text
message = Message(master, text='Dinh Quang Vuong\nCNTT15',width=200, bg='#0fff0f')
message.pack(anchor=E)

master.mainloop()