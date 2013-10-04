#stroplot.py
import pyfits as py
import numpy as n
import matplotlib.pyplot as plt
import parameters as par
reload(par)
vfs=1
f=open('lobe.out')
lines=f.readlines()
f.close()
last=0
qm=float(lines[last].split()[0])
ni=int(lines[last+1].split()[0])*2

xl=[]                                                  #Read Phase information
for i in n.arange(2,int(ni/8.0)+3,1):
    for j in n.arange(8):
        if (i-2)*8+j <ni:
            xl.append(float(lines[i].split()[j]))
last=int(ni/8.0)+3

yl=[]                                                  #Read Phase information
for i in n.arange(last,int(ni/8.0)+last+1,1):
    for j in n.arange(8):
        if (i-last)*8+j <ni:
            yl.append(float(lines[i].split()[j]))
last=last+int(ni/8.0)+3

dum=[]
for i in n.arange(last,int(ni/8.0)+last+1,1):
    for j in n.arange(8):
        if (i-last+2)*8+j <ni:
            dum.append(float(lines[i].split()[j]))
last=last+int(ni/8.0)
dum=[]
for i in n.arange(last-1,int(ni/8.0)+last,1):
    for j in n.arange(8):
        if (i-last+1)*8+j <ni:
            dum.append(float(lines[i].split()[j]))
last=last+int(ni/8.0)



np=int(lines[last].split()[0])
last+=1

xi,yi,vxi,vyi,vkxi,vkyi=[],[],[],[],[],[]
flag=0
for i in n.arange(last+1,len(lines)-1,1):
    if flag==0:
        temp=lines[i-1]+lines[i]
        flag=1
        
    else:
        temp=temp+lines[i]
wa=temp.split()

for i in n.arange(10000):
    xi.append(float(wa[i])), yi.append(float(wa[i+10000])),vxi.append(float(wa[i+20000])),vyi.append(float(wa[i+30000]))
    vkxi.append(float(wa[i+40000])),vkyi.append(float(wa[i+50000]))
    
az=n.arctan(n.array(yi)/n.array(xi))

for i in n.arange(len(az)):
    if xi[i]<0.0:
        az[i]=az[i]+xi[i]*n.pi
az=az*180/n.pi
porb=24*3600*par.porb           # in seconds
omega=2*n.pi/porb
gg=6.667e-8                     # Gravitational Constant, cgs
msun=1.989e33
cm=par.qm/(1.0+par.qm)
nvp=1000
vxp,vyp,vkxp,vkyp,rr=[],[],[],[],[]
inc=n.pi*par.inc/180.0
a=(gg*par.m1*msun*(1+qm))**(1./3)/omega**(2./3)     # Orbital Separation
vfs=1e5
vs=omega*a/vfs 
rd=0
i=0
r=1

vxi=vxi[0:i-1]
vyi=vyi[0:i-1]
vkxi=vkxi[0:i-1]
vkyi=vkyi[0:i-1]
az=az[0:i-1]
si=n.sin(inc)
vx=n.array(vxi)*si*vs
vy=n.array(vyi)*si*vs
vkx=n.array(vkxi)*si*vs
vky=n.array(vkyi)*si*vs
xl=n.array(xl)*vs*si
yl=n.array(yl)*vs*si
np=len(az)

# overplot stream
if par.stream == True : plt.plot(vx,vy,color=par.strcol) 
# overplot kepler velocity
if par.strcol == True : plt.plot(vkx,vky,color=par.strcol) 
# overplot lobe of M2

fig=plt.figure(1)

plt.show()