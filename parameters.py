#Orbital parameters file

# %%%%%%%%%%%%%%%%%%%    Input Files   %%%%%%%%%%%%%%%%%%%%%

base_dir='sdss1433'                # Base directory for input spectra
list='hjdfase02.dat'             # Name of the input file
dell=400                        # Delta in pixels to take as input spectra

# %%%%%%%%%%%%%%%%%%  Orbital Parameters   %%%%%%%%%%%%%%%%%%

object='J0644+3344'             # Name of the object
porb=0.054240679                      # Period in days
hjd0=53284.9766                 # HJD Zero point for fit
gama=-7.1                       # in km/s
# %%%%%%%%%%%%%%%%%%  Doppler Options   %%%%%%%%%%%%%%%%%%

lam0=6562.8                     # Wavelength zero in units of the original spectra
dellx=120
qm=0.067
inc=78.0
m1=0.87
# %%%%%%%%%%%%%%%%%%  Output Options   %%%%%%%%%%%%%%%%%%

psname='orie_1172'              # Name of output plot file 
output='pdf'                    # Can choose between: pdf, eps or png
data=False                      # If True then exit data will put in file *.txt
plot=True                       # Plot in Python window
plotlim=1.3                     # Plot limits. 1 = close fit.


# %%%%%%%%%%%%%%%%%%  Doppler Options   %%%%%%%%%%%%%%%%%%

stream=False                    # Plot Stream
lobes=True                    # Plot Lobes

strcol='black'                 # Stream color
lobcol='black'                 # Stream color