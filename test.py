# -*- coding:utf-8 -*-
from tkinter import *
from easy_gauge import *

root = Tk()
root.configure(bg='white')

def motion(event):
    x = event.x
    pa1.arrow_redraw(x)

pa1 = gauge(root,300)
pa1.pack(side=LEFT)
pa1.bgcolor = 'grey'
pa1.bg_redraw()
pa1.draw_scale(10,10,0,250)

root.bind('<Motion>', motion)
root.mainloop()
