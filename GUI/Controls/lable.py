from tkinter import *
import threading

win = Tk()

win.title('Day la Title')
# win.geometry('320x640+100+100')
# win.resizable(width=False, height=True)


#transparent
win.wm_attributes('-alpha',0.8)

scrH = win.winfo_screenheight()
scrW = win.winfo_screenwidth()
winH = 320
winW = 320

win.geometry("%dx%d+%d+%d"%(winW, winH, (scrW-winW)/2, (scrH-winH)/2))
win.configure(bg = '#7fff7f')



#Lable
lbl1 = Label(win, text='Lable left')
lbl1.pack(side = LEFT)
lbl2 = Label(win, text='Lable right')
lbl2.pack(side = RIGHT)

# def setText():
#     while True:
#         content = input()
#         lbl1.config(text = content)

# setTextThr = threading.Thread(target = setText)
# setTextThr.start()

win.mainloop()