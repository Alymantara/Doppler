#stroplot.py
import pyfits as py
import numpy as n
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import cataclysmic as cv
from matplotlib import mpl,pyplot
import matplotlib.cm as cm
import sys
import os as os
import glob
import mynormalize
import reamap as rm
plt.ion() # Activate update
import parameters as par
reload(par)
reload(rm)
cmaps=cm.gist_stern_r#cm.Greys_r# #cm.winter_r cm.Blues#cm.gist_stern
vfs=1
class DraggableColorbar(object):
    def __init__(self, cbar, mappable):
        self.cbar = cbar
        self.mappable = mappable
        self.press = None
        self.cycle = sorted([i for i in dir(plt.cm) if hasattr(getattr(plt.cm,i),'N')])
        self.index = self.cycle.index(cbar.get_cmap().name)

    def connect(self):
        """connect to all the events we need"""
        self.cidpress = self.cbar.patch.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.cbar.patch.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.cbar.patch.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)
        self.keypress = self.cbar.patch.figure.canvas.mpl_connect(
            'key_press_event', self.key_press)

    def on_press(self, event):
        """on button press we will see if the mouse is over us and store some data"""
        if event.inaxes != self.cbar.ax: return
        self.press = event.x, event.y

    def key_press(self, event):
        if event.key=='down':
            self.index += 1
        elif event.key=='up':
            self.index -= 1
        if self.index<0:
            self.index = len(self.cycle)
        elif self.index>=len(self.cycle):
            self.index = 0
        cmap = self.cycle[self.index]
        self.cbar.set_cmap(cmap)
        self.cbar.draw_all()
        self.mappable.set_cmap(cmap)
        #self.mappable.get_axes().set_title(cmap)
        self.cbar.patch.figure.canvas.draw()

    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.press is None: return
        if event.inaxes != self.cbar.ax: return
        xprev, yprev = self.press
        dx = event.x - xprev
        dy = event.y - yprev
        self.press = event.x,event.y
        #print 'x0=%f, xpress=%f, event.xdata=%f, dx=%f, x0+dx=%f'%(x0, xpress, event.xdata, dx, x0+dx)
        scale = self.cbar.norm.vmax - self.cbar.norm.vmin
        perc = 0.03
        if event.button==1:
            self.cbar.norm.vmin -= (perc*scale)*n.sign(dy)
            self.cbar.norm.vmax -= (perc*scale)*n.sign(dy)
        elif event.button==3:
            self.cbar.norm.vmin -= (perc*scale)*n.sign(dy)
            self.cbar.norm.vmax += (perc*scale)*n.sign(dy)
        self.cbar.draw_all()
        self.mappable.set_norm(self.cbar.norm)
        self.cbar.patch.figure.canvas.draw()


    def on_release(self, event):
        """on release we reset the press data"""
        self.press = None
        self.mappable.set_norm(self.cbar.norm)
        self.cbar.patch.figure.canvas.draw()

    def disconnect(self):
        """disconnect all the stored connection ids"""
        self.cbar.patch.figure.canvas.mpl_disconnect(self.cidpress)
        self.cbar.patch.figure.canvas.mpl_disconnect(self.cidrelease)
        self.cbar.patch.figure.canvas.mpl_disconnect(self.cidmotion)

va=1
vxy=(2.0*n.arange(rm.nv)/(rm.nv-1)-1)*rm.va/1e5
dv=vxy[1]-vxy[0]
vxy=n.concatenate([[vxy[0]-dv/2],vxy+dv/2.0])

im=rm.im


fig=plt.figure(1)
plt.clf()
x,y = n.ogrid[vxy[0]:vxy[-1]:dv,vxy[0]:vxy[-1]:dv]
img = plt.imshow(im,extent=(y.min(), y.max(),x.min(), x.max()),interpolation='nearest', cmap=cmaps,aspect='auto',origin='lower')            
plt.xlabel('V$_x$ km s$^{-1}$')
plt.ylabel('V$_y$ km s$^{-1}$')
cbar = plt.colorbar(format='%05.2f')
cbar.set_label('Arbitrary Flux')
cbar.set_norm(mynormalize.MyNormalize(vmin=im.min(),vmax=im.max(),stretch='linear'))
cbar = DraggableColorbar(cbar,img)
cbar.connect()

import stroplot as st
reload(st)
if par.lobes == True:
    plt.plot(-st.yl,st.xl,color=par.lobcol)
    ple=n.array([-0.1,0.1])*st.vs
    #mark center of mass with plus
    ze=[0,0]
    plt.plot(0,0,color=par.lobcol,marker='x',markersize=10)
    vy1=st.cm*st.vs*st.si
    #mark M2 with cross
    pler=0.7*ple
    m2y=n.array([1-st.cm,1-st.cm])*st.vs*st.si
    plt.plot(0,m2y[0],color=par.lobcol,marker='+',markersize=10)

    #mark M1 with cross
    m1y=n.array([-1,-1])*st.vy1*st.vs*st.si
    plt.plot(0,-vy1,color=par.lobcol,marker='+',markersize=10)
    #plt.plot(st.vx,st.vy,color=par.strcol) 
    #plt.plot(st.vkx,st.vky,color=par.strcol)
plt.show()