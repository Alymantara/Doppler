#reamap.py
import numpy as n
import matplotlib.pyplot as plt


f=open('dop.out')
lines=f.readlines()
f.close()
nph,nvp,nv,w0,aa=int(lines[0].split()[0]),int(lines[0].split()[1]),int(lines[0].split()[2]),float(lines[0].split()[3]),float(lines[0].split()[4])
gamma,abso,atm,dirin=float(lines[1].split()[0]),lines[1].split()[1],lines[1].split()[2],lines[1].split()[3]


pha=[]                                                  #Read Phase information
for i in n.arange(2,int(nph/8.0)+3,1):
    for j in n.arange(8):
        if (i-2)*8+j <nph:
            pha.append(float(lines[i].split()[j]))
last=int(nph/8.0)+3
pha=n.array(pha)/2.0/n.pi   

dpha=[]
if int(lines[last].split()[0])==1:
    for i in n.arange(last+1,int(nph/8.0)+last+3,1):
        for j in n.arange(8):
            if (i-last-1)*8+j <nph:
                dpha.append(float(lines[i].split()[j]))
dpha=n.array(dpha)/2.0/n.pi   

last=int(nph/8.0)+last+3

vp=[]
for i in n.arange(last-1,int(nvp/8.0)+last+3,1):
    for j in n.arange(8):
        if (i-last+1)*8+j <nvp:
            vp.append(float(lines[i].split()[j]))
last=int(nvp/8.0)+last+3
vp=n.array(vp)
dvp=vp[1]-vp[0]
vp=vp-dvp/2.0

dm=[]           # Read the spectrum
flag=0
for i in n.arange(last-2,int(nvp*nph/8.0)+last-2,1):
    if flag==0:
        temp=lines[i-1]+lines[i]
        flag=1
        
    else:
        temp=temp+lines[i]
temp1=temp.split()
for i in temp1:
    dm.append(float(i))
dm=n.array(dm)
dm=dm.reshape(nvp,nph)
last=int(nvp*nph/8.0)+last-2

ih,iw,pb0,pb1,ns,ac,al,clim,norm,wid,af=int(lines[last].split()[0]),int(lines[last].split()[1]),float(lines[last].split()[2]),float(lines[last].split()[3]),int(lines[last].split()[4]),float(lines[last].split()[5]),float(lines[last].split()[6]),float(lines[last].split()[7]),int(lines[last].split()[8]),float(lines[last].split()[9]),float(lines[last].split()[10])
nv,va=int(lines[last+1].split()[0]),float(lines[last+1].split()[1])


last=last+2
#  READ IMAGE

im=[]
flag=0
for i in n.arange(last+1,int(nv*nv/6.0)+last+1,1):
    if flag==0:
        temp=lines[i-1]+lines[i]
        flag=1
        
    else:
        temp=temp+lines[i]
temp1=temp.split()
for i in temp1:
    im.append(float(i))
im=n.array(im)
im=im.reshape(nv,nv)
last=int(nv*nv/6.0)+last+1

ndum=int(lines[last].split()[0])
dmr=[]           # Read the Reconstructed spectrum
flag=0
for i in n.arange(last+2,int(nvp*nph/6.0)+last+1,1):
    if flag==0:
        temp=lines[i-1]+lines[i]
        flag=1
        
    else:
        temp=temp+lines[i]
temp1=temp.split()
for i in temp1:
    dmr.append(float(i))
dmr=n.array(dmr)
dmr=dmr.reshape(nvp,nph)
last=int(nvp*nph/6.0)+last+1

ndum=int(lines[last].split()[0])

dpx=[]
flag=0
for i in n.arange(last+2,int(nv*nv/6.0)+last+2,1):
    if flag==0:
        temp=lines[i-1]+lines[i]
        flag=1
        
    else:
        temp=temp+lines[i]
temp1=temp.split()
for i in temp1:
    dpx.append(float(i))
dpx=n.array(dpx)
dpx=dpx.reshape(nv,nv)







