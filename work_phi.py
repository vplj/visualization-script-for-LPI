import sdf
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
#from numpy import ma
from matplotlib import colors, ticker, cm
from matplotlib.mlab import bivariate_normal
from optparse import OptionParser
import os
import matplotlib.colors as mcolors 

######## Constant defined here ########
pi        =     3.1415926535897932384626
q0        =     1.602176565e-19 # C
m0        =     9.10938291e-31  # kg
v0        =     2.99792458e8    # m/s^2
kb        =     1.3806488e-23   # J/K
mu0       =     4.0e-7*pi       # N/A^2
epsilon0  =     8.8541878176203899e-12 # F/m
h_planck  =     6.62606957e-34  # J s
wavelength=     1.0e-6
frequency =     v0*2*pi/wavelength

exunit    =     m0*v0*frequency/q0
bxunit    =     m0*frequency/q0
denunit    =     frequency**2*epsilon0*m0/q0**2
print('electric field unit: '+str(exunit))
print('magnetic field unit: '+str(bxunit))
print('density unit nc: '+str(denunit))

font = {'family' : 'monospace',  
        'style'  : 'normal',
        'color'  : 'black',  
	    'weight' : 'normal',  
        'size'   : 14,  
       }  
######### Parameter you should set ###########
start   =  50  # start time
stop    =  1299  # end time
step    =  1  # the interval or step

to_path = './jpg_1300/'

directory = './txt_1300/'
px_y = np.loadtxt(directory+'px2d_down.txt')
py_y = np.loadtxt(directory+'py2d_down.txt')
xx_y = np.loadtxt(directory+'xx2d_down.txt')
yy_y = np.loadtxt(directory+'yy2d_down.txt')
workx2d_y = np.loadtxt(directory+'workx2d_down.txt')
worky2d_y = np.loadtxt(directory+'worky2d_down.txt')
fieldex_y = np.loadtxt(directory+'fieldex2d_down.txt')
fieldey_y = np.loadtxt(directory+'fieldey2d_down.txt')
fieldbz_y = np.loadtxt(directory+'fieldbz2d_down.txt')



gg_y = (px_y**2+py_y**2+1)**0.5
R_y  = gg_y-px_y

phi_y = (np.linspace(5.0,125.0,1201)-xx_y)%1.0




color_y = np.zeros_like(phi_y[:,0])


for i in range(0,color_y.size):
    color_y[i] = phi_y[i,np.argmax( (xx_y[i,:] > 5.0) & (abs(yy_y[i,:])<3.2)  ) ]


#for i in range(0,color_y.size):
#    color_y[i] = R_y[i,np.argmax( xx_y[i,:] > 5.0  )]

#for i in range(0,color_x.size):
#    color_x[i] = R_x[i,np.argmax( xx_x[i,:] > 5.0  )]

print(color_y)

for n in range(start,stop+step,step):
    #### header data ####
#    plt.subplot()
    plt.scatter(workx2d_y[:,n-start], worky2d_y[:,n-start], c=abs(color_y), norm=colors.Normalize(vmin=0.0, vmax=1.0), s=40, cmap='rainbow', edgecolors='black', alpha=0.6)
    cbar=plt.colorbar()
    cbar.set_label(r'$\phi$ for injecting time',fontdict=font)

    plt.plot(np.linspace(-500,900,1001), np.zeros([1001]),':k',linewidth=1.5)
    plt.plot(np.zeros([1001]), np.linspace(-500,900,1001),':k',linewidth=1.5)
    plt.plot(np.linspace(-500,900,1001), np.linspace(-500,900,1001),':k',linewidth=1.5)
 #   plt.legend(loc='upper right')
    plt.xlim(-200,600)
    plt.ylim(-200,600)
    plt.xlabel(r'$Work_x [m_ec^2]$',fontdict=font)
    plt.ylabel(r'$Work_y [m_ec^2]$',fontdict=font)
    #plt.xticks(fontsize=20); plt.yticks(fontsize=20);
    #plt.title('electron at y='+str(round(y[n,0]/2/np.pi,4)),fontdict=font)

    #plt.show()
    #lt.figure(figsize=(100,100))
    fig = plt.gcf()
    fig.set_size_inches(8, 6.5)
    fig.savefig(to_path+'work_phi_down'+str(n).zfill(4)+'.png',format='png',dpi=160)
    plt.close("all")

    print('finised '+str(round(100.0*(n-start+step)/(stop-start+step),4))+'%')
