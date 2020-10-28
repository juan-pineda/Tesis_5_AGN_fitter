#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys,os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy import units as u
import astropy.constants as const
import scipy
from matplotlib import gridspec
from astropy.io import fits
import pickle
from pickle import *
import time
import math
import re
from astropy.table import Table
import itertools

# In[ ]:

def RADIO(LIR, conv_factor, sb_nu0, sb_Fnu0): #, rad_excess):
    
    q_IR_r14 = 2.64 #+ np.random.normal(2.64, 0.26,1)
    alpha_syn  = -0.75
    alpha_th = -0.1
    nth_frac =0.9

    L14 = 10**(np.log10(LIR*conv_factor)-q_IR_r14)/3.75e12 #1.4e9 #to Wats
    nu_spacing= (np.log10(sb_nu0)[2]-np.log10(sb_nu0)[1])
    radio_points = (np.log10(sb_nu0)[0]-9)/nu_spacing
    radio_nu14= np.log10(1.4e9)

    radio_nu = np.arange(np.log10(sb_nu0)[0]- nu_spacing*int(radio_points),np.log10(sb_nu0)[0], nu_spacing)
    radio_SB_nu = np.concatenate((radio_nu, np.log10(sb_nu0)[:np.argmax(sb_Fnu0)]))
    #optical_nu = np.arange(np.log10(sb_nu0)[-1], 16, nu_spacing)
    #radio_opt_nu = np.concatenate((radio_nu, np.log10(sb_nu0), optical_nu))
    radio_IR_nu = np.concatenate((radio_nu, np.log10(sb_nu0)))

    Lsb = np.concatenate((sb_Fnu0[0]*1e-4*np.ones(len(radio_nu)),sb_Fnu0)) #, sb_Fnu0[-1]*1e-4*np.ones(len(optical_nu))))

    Lsyn_0 = 10**(-1*alpha_syn* np.log10(1.4e9/10**radio_SB_nu[0])) * L14*(nth_frac)
    Lsyn_SB = Lsyn_0 * 10**(alpha_syn* np.log10(10**radio_SB_nu/10**radio_SB_nu[0])) 
    Lsyn = np.concatenate((Lsyn_SB, 0*np.ones(len(radio_IR_nu)-len(Lsyn_SB))))

    Lth_0 = 10**(-1*alpha_th* np.log10(1.4e9/10**radio_SB_nu[0])) * L14*(1.-nth_frac)
    Lth_SB= Lth_0* 10**(alpha_th* np.log10(10**radio_SB_nu/10**radio_SB_nu[0]))  
    Lth = np.concatenate((Lth_SB, 0*np.ones(len(radio_IR_nu)-len(Lth_SB))))

    #Lsyn_AGN = RAD_excess*L14*10**(alpha_syn* np.log10(10**radio_opt_nu/10**radio_opt_nu[0]))
    Lir_rad= Lir_rad= Lsb+Lsyn+Lth #Lsb+Lsyn+Lth+Lsyn_AGN

    return  radio_IR_nu, Lir_rad #radio_nu_syn, Lir_rad   all_nu, Lir_rad


dusttable = Table.read('Models/s17_lowvsg_dust.fits')
pahstable = Table.read('Models/s17_lowvsg_pah.fits')
Dwl, DnuLnu = dusttable['LAM'],dusttable['SED'] #micron, Lsun
Pwl, PnuLnu = pahstable['LAM'],pahstable['SED'] #micron, Lsun
Tdust = np.array(dusttable['TDUST'])[0] #K
LIR=  np.array(dusttable['LIR'])[0]*3.826e33
fracPAH = np.concatenate(((np.arange(0.0, 0.1, 0.01)/100.),(np.arange(0.1, 5.5, 0.1)/100.)))
RADexc= np.logspace(-1, 3, 10) #np.arange(10, 110, 10)

idxs=[np.arange(len(Tdust)), np.arange(len(fracPAH))] #,np.arange(len(RADexc))]
par_idxs_combinations = np.array(list(itertools.product(*idxs)))
conv_factor= 3.826e-33 #1e-6
Dnu= (Dwl[0] * u.micron).to(u.Hz, equivalencies=u.spectral())
Pnu= (Pwl[0] * u.micron).to(u.Hz, equivalencies=u.spectral())
DLnu= np.array(DnuLnu[0])/Dnu #*conv_factor #* u.Lsun.to(u.W)
PLnu=np.array(PnuLnu[0])/Pnu #*conv_factor#* u.Lsun.to(u.W)


column_names = ["frequency", 'SED', 'fracPAH-values', 'Tdust-values', 'LIR'] #, 'RADexc-values']  #To create the columns of the dataframe
S17_radio = pd.DataFrame(columns = column_names)
j = 0

for c in par_idxs_combinations:
    t=c[0]
    fp=c[1]
    #re=c[2]

    sb_nu0 = np.array(Dnu[t,:])[::-1]
    sb_Fnu0 = np.array( (1-fracPAH[fp]) * DLnu[t,:] + (fracPAH[fp]) * PLnu[t,:])[::-1]

    rad_sb_nu0 ,rad_sb_Fnu0= RADIO(LIR[t], conv_factor, sb_nu0, sb_Fnu0) #, RADexc[re]) 

    New_row = {'SED': rad_sb_Fnu0, 'frequency': rad_sb_nu0, 'fracPAH-values': fracPAH[fp], 'Tdust-values': Tdust[t], 'LIR': LIR[t]}# ,'RADexc-values': RADexc[re]} 
    S17_radio = S17_radio.append(New_row, ignore_index = True) 

    j += 1
    if j == 1920:
        print('20% of the finished process...')
    elif j == 3840:
        print('40% of the finished process...')
    elif j == 5760:
        print('60% of the finished process...')
    elif j == 7680:
        print('80% of the finished process...')
    elif j == 9599:
        print('Completed process.')


f2 = open('Models/S17_radiolight.pickle', 'wb')
pickle.dump(S17_radio, f2, protocol= pickle.HIGHEST_PROTOCOL) #2
f2.close()


