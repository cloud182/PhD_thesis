import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import sys

sync = np.genfromtxt('fort12_sync.dat', unpack=True)
fort12g = np.genfromtxt('fort12g.dat', unpack = True)
fort12d = np.genfromtxt('fort12d.dat', unpack = True)
fort12_600d = np.genfromtxt('fort12_600d.dat', unpack = True)
fort12_600g = np.genfromtxt('fort12_600g.dat', unpack = True)
fort12_100g = np.genfromtxt('fort12_100g.dat', unpack = True)
fort12_100d = np.genfromtxt('fort12_100d.dat', unpack = True)
fort18 = np.genfromtxt('fort18.dat', unpack = True)
fort113_ic2 = np.genfromtxt('fort113_ic2.dat', unpack = True)
fort113_ic3 = np.genfromtxt('fort113_ic3.dat', unpack = True) 
n7212con = np.genfromtxt('n7212cont.dat', unpack = True)

#### summing black bodies
x_new = np.arange(10.0,16.,0.08)
a=np.zeros(17)
fort113_2=10**(fort113_ic2[1]-13.5)
aa=np.append(fort113_2,a)
fort113_3=10**(fort113_ic3[1]-19.3)
galaxy = np.log10(aa+fort113_3) 

#### summing free-free

x_f = fort12g[0]
free1 = 10**(fort12g[1]-9.5)
free2 = 10**(fort12_100g[1]-8.)
free3 = 10**(fort12_600g[1]-10.5)
free = np.log10(free1+free3)

#### summing dust

x_d = fort12d[0]
dust1 = 10**(fort12d[1]-11.3)
dust2 = 10**(fort12_100d[1]-12)
dust3 = 10**(fort12_600d[1]-11.3)
dust = np.log10(dust1+dust2+dust3)

#### interpolation of the data
galaxy_i = interp1d(x_new,galaxy)
sync_i = interp1d(sync[0],sync[1])
fort18_i = interp1d(fort18[0],fort18[1])
free_i = interp1d(x_f, free)
dust_i = interp1d(x_d, dust)
agn_i = interp1d(fort18[0], fort18[1])

x_new_d = np.arange(10.04,14.69,0.08)
new_dust = 10**dust_i(x_new_d)
x_new_f = np.arange(8.04,19.25,0.08)
new_free = 10**free_i(x_new_f)
x_new_s = np.arange(7,12.93,0.08)
new_sync = 10**(sync_i(x_new_s)-9.5)
x_new_a = np.arange(15.32,19.97,0.08)
new_agn = 10**(agn_i(x_new_a)-13.3)
x_new_g = np.arange(10.04,15.89,0.08)
new_gal = 10**(galaxy_i(x_new_g))

## da 7 a 20.04###
x_def = np.arange(7,20.03,0.08)
a_d = np.zeros(41)
a_d_f = np.zeros(63)
new_dust = np.append(a_d,new_dust)
new_dust = np.append(new_dust,a_d_f)
a_f = np.zeros(13)
a_f_f = np.zeros(9)
new_free = np.append(a_f,new_free)
new_free = np.append(new_free, a_f_f)
a_s_f = np.zeros(88)
new_sync = np.append(new_sync,a_s_f)
a_a = np.zeros(104)
new_agn = np.append(a_a,new_agn)
a_g = np.zeros(36)
a_g_f = np.zeros(53)
new_gal = np.append(a_g,new_gal)
new_gal = np.append(new_gal,a_g_f)

total_sed = np.log10(new_dust+new_free+new_sync+new_agn+new_gal)






fig, ax = plt.subplots(1,1)
ax.axis([7,20,-16.5,-8.])
ax.plot(x_def,total_sed, c='k', label='Best fit')
ax.plot(fort18[0],fort18[1]-13.3, c='c', ls = '--',label='AGN')
ax.plot(x_f,free, c='orange', ls= '--', label='Free-free')
ax.plot(x_d+0.24,dust, c='y', ls= '--', label='Dust')
ax.plot(x_new-0.16,galaxy, c='r', ls = '--', label='Galaxy Stars')
ax.plot(sync[0],sync[1]-9.5, c='b', ls= '--', label='Syncrothron')
ax.errorbar(np.log10(n7212con[0]),np.log10(n7212con[1])+0.89,yerr=0, ls = '', marker = 'o', markerfacecolor = 'none', markeredgecolor='k', label = 'NGC 7212')
ax.legend(loc='best')
ax.set_xlabel('log($\\nu$) (Hz)')
ax.set_ylabel('log($\\nu$F$_{\\nu}$) (erg cm$^{-2}$ s$^{-1}$)')
ax.set_title('NGC 7212')
#plt.show()
plt.savefig('sedn72n.pdf')
plt.close()
