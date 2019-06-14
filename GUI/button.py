from tkinter import *

def up():
    btnUp['bg'] = 'green'
    print("UP")

def down():
    print("DOWN")

def left():
    print("LEFT")

def right():
    print("RIGHT")

win = Tk()

frame1 = Frame(win)
frame1.pack()

frame2 = Frame(win)
frame2.pack()

frame3 = Frame(win)
frame3.pack()

btnUp = Button(frame1, text = 'UP', command = up, bg = 'red', fg = 'white')
btnUp.pack()

btnLeft = Button(frame2, text = 'LEFT', command = left)
btnLeft.pack(side = LEFT)

btnRight = Button(frame2, text = 'RIGHT', command = right)
btnRight.pack(side = RIGHT)

btnDown = Button(frame3, text = 'DOWN', command = down)
btnDown.pack()

win.mainloop()