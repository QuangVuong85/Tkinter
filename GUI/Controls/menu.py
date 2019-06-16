from tkinter import *

master = Tk()

# create a toplevel menu
menubar = Menu(master)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", accelerator="Ctrl+O")
filemenu.add_command(label="Save", accelerator="Ctrl+S")
filemenu.add_command(label="Save as", accelerator="Ctrl+Shift+S")
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator="Alt+F4")
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
editmenu.add_separator()
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Cut")
menubar.add_cascade(label="Edit", menu=editmenu)

menubar.add_cascade(label="View")
menubar.add_cascade(label="Help")

# display the menu
master.config(menu=menubar)

text = Text(master)
text.place(relheight="1.0", relwidth="1.0")


master.mainloop()