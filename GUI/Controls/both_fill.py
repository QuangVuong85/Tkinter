import tkinter as tk
import random as rd

### fill = NONE or X or Y or BOTH

master = tk.Tk()
master.title("tkinter LEFT,RIGHT,TOP,BOTTOM")
master.geometry("300x300")
# master.resizable(width=False, height=False)

###
# btnLeft = tk.Button(master, text = "LEFT")
# btnLeft.pack(side = tk.LEFT, fill = tk.BOTH)

# btnTop = tk.Button(master, text = "TOP")
# btnTop.pack(side = tk.TOP, fill = tk.BOTH)

# btnRight = tk.Button(master, text = "RIGHT")
# btnRight.pack(side = tk.RIGHT, fill = tk.BOTH)

# btnBottom = tk.Button(master, text = "BOTTOM")
# btnBottom.pack(side = tk.BOTTOM, fill = tk.BOTH)

###
def line():
    x1 = rd.randrange(0, 300)
    y1 = rd.randrange(0, 300)
    x2 = rd.randrange(0, 300)
    y2 = rd.randrange(0, 300)
    canvas.create_line(x1, y2, x2, y2)

canvas = tk.Canvas(master, width=300, height=300, bg = "green")
canvas.pack(fill = tk.BOTH)

btn = tk.Button(master, text="Draw", command=line).pack(side = tk.BOTTOM, fill = tk.BOTH)

master.mainloop()