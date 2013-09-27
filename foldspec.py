#! Python Foldspec

import numpy as n
import parameters as par
reload(par)


def foldspec(rebin=True,nbins=None):
   
    
    nbins=None
    inputs=n.loadtxt(par.base_dir+'/'+par.list,dtype={'names': ('files', 'phase'),'formats': ('S11', 'f4')})

    # Check 1st spectrum and get wavelength to interpolate
    w1st=n.loadtxt(par.base_dir+'/'+inputs[0]['files'],unpack=True)
    if nbins==None:
        nbins=len(inputs)*1.5    #By default 
    wave,flux=[],[]
    for i in inputs:
        print i['files']+'  '+str(i['phase'])
        w,f=n.loadtxt(par.base_dir+'/'+i['files'],unpack=True)
        #Missing interpolation in the case of different dispersion in wavelength
        wave.append(w),flux.append(f)
    delp=1.0/nbins
    pha=n.arange(0,1,delp)    


    return(wave,flux,pha,inputs['phase'],inputs['phase'],delp,inputs['files'])

n.save('foldspec',foldspec())