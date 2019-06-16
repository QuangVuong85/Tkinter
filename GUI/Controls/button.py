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

# frame1 = Frame(win)
# frame1.pack()
# frame2 = Frame(win)
# frame2.pack()
# frame3 = Frame(win)
# frame3.pack()

# btnUp = Button(frame1, text = 'UP', command = up, bg = 'red', fg = 'white')
# btnUp.pack()
# btnLeft = Button(frame2, text = 'LEFT', command = left)
# btnLeft.pack(side = LEFT)
# btnRight = Button(frame2, text = 'RIGHT', command = right)
# btnRight.pack(side = RIGHT)
# btnDown = Button(frame3, text = 'DOWN', command = down)
# btnDown.pack()

### ipadx, ipady, padx, pady
# btnDown = Button(win, text = 'DOWN_FILL', command = down, bg="yellow")
# btnDown.pack(side = BOTTOM, fill = X, ipady=10, pady=20)

### anchor = NSEW
btnDown1 = Button(win, text = 'DOWN_ANCHOR', command = down, bg="yellow")
btnDown1.pack(anchor=SE)

win.mainloop()