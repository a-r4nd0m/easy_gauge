# -*- coding:utf-8 -*-
from tkinter import *
from easy_gauge import *

root = Tk()
#root.configure(bg='black')
panel  = Frame(root, bg = 'black')
panel.pack()
def motion(event):
    global x0
    global y0
    x,y = event.x,event.y
    pa1.arrow_redraw(x)
    pa2.arrow_redraw(y/100)
    fld.create_line(x0,y0,x,y)
    x0,y0 = x,y

pa1 = gauge(panel,250)
pa1.pack(side=LEFT)
pa1.bgcolor = 'black'
pa1.linecolor = 'white'
pa1.arrowcolor = 'green'
pa1.bg_redraw()
pa1.draw_scale(10,5,0,500)

pa2 = gauge(panel,250)
pa2.pack()
pa2.bgcolor = 'black'
pa2.linecolor = 'gold'
pa2.arrowcolor = 'red'
pa2.bg_redraw()
pa2.draw_scale(10,5,0,2.5)
x0,y0 = 0,0
fld = Canvas(root, width = 500, height = 250)
fld.pack(side=TOP)
fld.bind('<Motion>', motion)
root.mainloop()
