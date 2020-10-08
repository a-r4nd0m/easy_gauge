# -*- coding:utf-8 -*-

from tkinter import *
from math import sin,cos,pi

class gauge(Canvas):
    def __init__ (self,par,size):
        self.arrowcolor = 'red'
        self.bgcolor = 'white'
        self.linecolor = 'black'
        self.size = size
        Canvas.__init__ (self,
                         par, width = size,
                         height = size,
                         bg = par["bg"],
                         highlightthickness=0)
        
    
    def draw_scale(self,N,n,value_min,value_max):
        self.delete('scale')
        self.value_min = value_min
        self.value_max = value_max
        da = 270/N
        dv =(value_max-value_min)/N
        R = self.size/2
        for i in range(0,N+1):
            xm = cos(da*i*pi/180-pi/4)
            ym = sin(da*i*pi/180-pi/4)
            self.create_line(R-R*xm*0.85,R-R*ym*0.85,R-R*xm,R-R*ym,fill = self.linecolor,width = 3,tag = 'scale')
            value = i*dv+value_min
            T = str('%.1F'%value)
            if T[-2:]=='.0':
                T = T[:-2]
            self.create_text(R-R*xm*0.75,R-R*ym*0.75,text = T,fill = self.linecolor,tag = 'scale')
        da = da/n
        for i in range(0,n*N+1):
            xm = cos(da*i*pi/180-pi/4)
            ym = sin(da*i*pi/180-pi/4)
            self.create_line(R-R*xm*0.92,R-R*ym*0.92,R-R*xm,R-R*ym,fill = self.linecolor,width = 2,tag = 'scale')

    def arrow_redraw(self,value):
        R = self.size/2
        value = value-self.value_min
        a = 270*value/(self.value_max-self.value_min)
        if a>280:
            a = 280
        if a<-10:
            a = -10
        x = 1-cos(a*pi/180-pi/4)*0.92
        y = 1-sin(a*pi/180-pi/4)*0.92
        self.delete('arrow')
        self.create_line(R,R,R*x,R*y,fill = self.arrowcolor,width = 2,tag = 'arrow')#, arrow = LAST)
        self.create_oval(R*0.95,R*0.95,R*1.05,R*1.05,fill = self.linecolor, outline = self.linecolor,tag = 'arrow')

    def bg_redraw(self):
        self.delete('bg')
        self.create_oval(0,0,self.size,self.size,
                         outline = self.bgcolor,
                         fill = self.bgcolor,
                         tag = 'bg')



