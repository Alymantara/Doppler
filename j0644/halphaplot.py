import matplotlib.pyplot as m
import numpy as n
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
import matplotlib.pyplot as m
rc('text', usetex=True)

w0,f0=n.loadtxt('csum0.txt',unpack=True)
w1,f1=n.loadtxt('csum1.txt',unpack=True)
w2,f2=n.loadtxt('csum2.txt',unpack=True)
w3,f3=n.loadtxt('csum3.txt',unpack=True)
w4,f4=n.loadtxt('csum4.txt',unpack=True)
w5,f5=n.loadtxt('csum5.txt',unpack=True)
w6,f6=n.loadtxt('csum6.txt',unpack=True)
w7,f7=n.loadtxt('csum7.txt',unpack=True)
w8,f8=n.loadtxt('csum8.txt',unpack=True)

m.axis([6520,6600,0,1800])
m.plot(w0,f0,'k')
m.plot(w1,f1,'k',markersize=2)
m.plot(w2,f2,'k',markersize=2)
m.plot(w3,f3,'k',markersize=2)
m.plot(w4,f4,'k',markersize=2)
m.plot(w5,f5,'k',markersize=2)
m.plot(w6,f6,'k',markersize=2)
m.plot(w7,f7,'k',markersize=2)
m.plot(w8,f8,'k',markersize=2)
m.xlabel('Longitud de Onda, Angstrom')
m.ylabel('Flujo Relativo',fontsize='medium')
m.text(6580,80,'Fase 0.0')
m.text(6580,230,'Fase 0.125')
m.text(6580,400,'Fase 0.25')
m.text(6580,610,'Fase 0.375')
m.text(6580,820,'Fase 0.5')
m.text(6580,1020,'Fase 0.625')
m.text(6580,1190,'Fase 0.75')
m.text(6580,1390,'Fase 0.875')
m.text(6580,1569,'Fase 1.0')



