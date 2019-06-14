from tkinter import *

def printxy():
    print('CLICK')

win = Tk()

for i in range(5):
    for j in range(5):
        Button(win, text = '(%d, %d)'%(i,j), bg = 'red', font = 'Times 20', command = printxy).grid(column = j, row = i)

Button(win, text = '6', bg = 'red', font = 'Times 20', command = printxy).grid(row = 6, columnspan = 6, sticky = W)
Button(win, text = '6', bg = 'red', font = 'Times 20', command = printxy).grid(row = 6, columnspan = 6, sticky = E)

win.mainloop()