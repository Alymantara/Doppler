pro stack_he2
del=0.0625
readcol,'hefasetotal.dat',spec,phase,velrad,format='A,D,D'
n=n_elements(spec)
i0=0
i1=0
i2=0
i3=0
i4=0
i5=0
i6=0
i7=0
i8=0
i9=0
for i=0,n-1 do begin
   if i eq 0 then begin
   readcol,spec[0],w,f
   cosum0=f*0
   cosum1=f*0
   cosum2=f*0
   cosum3=f*0
   cosum4=f*0
   cosum5=f*0
   cosum6=f*0
   cosum7=f*0
   cosum8=f*0
   cosum9=f*0
endif
if phase[i] ge 0.125-del && phase[i] lt 0.125+del then begin
      readcol,spec[i],w,f,/silent
      cosum0=cosum0+f
      w0=w
      i0=i0+1
endif
if phase[i] ge 0.25-del && phase[i] lt 0.25+del then begin
      readcol,spec[i],w,f,/silent
      cosum1=cosum1+f
      w1=w
      i1=i1+1
   endif
if phase[i] ge 0.365-del && phase[i] lt 0.365+del then begin
      readcol,spec[i],w,f,/silent
      cosum2=cosum2+f
      w2=w
      i2=i2+1
   endif
if phase[i] ge 0.50-del && phase[i] lt 0.50+del then begin
      readcol,spec[i],w,f,/silent
      cosum3=cosum3+f
      w3=w
      i3=i3+1
   endif
if phase[i] ge 0.625-del && phase[i] lt 0.6250+del then begin
      readcol,spec[i],w,f,/silent
      cosum4=cosum4+f
      w4=w
      i4=i4+1
   endif
if phase[i] ge 0.75-del && phase[i] lt 0.75+del then begin
      readcol,spec[i],w,f,/silent
      cosum5=cosum5+f
      w5=w
      i5=i5+1
   endif
if phase[i] ge 0.875-del && phase[i] lt 0.875+del then begin
      readcol,spec[i],w,f,/silent
      cosum6=cosum6+f
      w6=w
      i6=i6+1
   endif
if phase[i] ge 0.875+del || phase[i] lt del then begin
      readcol,spec[i],w,f,/silent
      cosum7=cosum7+f
      w7=w
      i7=i7+1
   endif
endfor

plot,w7,cosum7/i7,yra=[00,820],xra=[4686.3-40,4686.3+30],ystyle=1
oplot,w0,cosum0/i0+70
oplot,w1,cosum1/i1+160
oplot,w2,cosum2/i2+250
oplot,w3,cosum3/i3+360
oplot,w4,cosum4/i4+430
oplot,w5,cosum5/i5+520
oplot,w6,cosum6/i6+610
oplot,w7,cosum7/i7+700


;Print files for spectra
forprint,w0,cosum0/i0+70,/NOCOMMENT,textout='he2sum0.txt'
forprint,w1,cosum1/i1+160,/NOCOMMENT,textout='he2sum1.txt'
forprint,w2,cosum2/i2+250,/NOCOMMENT,textout='he2sum2.txt'
forprint,w3,cosum3/i3+360,/NOCOMMENT,textout='he2sum3.txt'
forprint,w4,cosum4/i4+430,/NOCOMMENT,textout='he2sum4.txt'
forprint,w5,cosum5/i5+520,/NOCOMMENT,textout='he2sum5.txt'
forprint,w6,cosum6/i6+610,/NOCOMMENT,textout='he2sum6.txt'
forprint,w7,cosum7/i7,/NOCOMMENT,textout='he2sum7.txt'
forprint,w7,cosum7/i7+700,/NOCOMMENT,textout='he2sum8.txt'


print,i0,i1,i2,i3,i4,i5,i6,i7
end
