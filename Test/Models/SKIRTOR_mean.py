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


# In[ ]:


column_names = ["wavelength", 'SED', 'incl-values', 'Dm-values']  #To create the columns of the dataframe
SKIRTOR = pd.DataFrame(columns = column_names)
DustM = pd.read_csv("Models/SKIRTOR/total_dust_mass_2016-7-18.txt", sep = '    ', decimal=".", names= ['model', 'Mass'], skiprows = 2, engine = 'python')
count = 0
N_SEDs = 1600 #10 incl, 80 incl+oa, 400 incl+oa+tv, 1600 incl+oa+tv+p
SEDs = [np.zeros((132))]*N_SEDs #10 just incl 
Mds = np.zeros((N_SEDs))

for i in os.listdir("Models/SKIRTOR/skirtor_2016-7-18"):
    data = pd.read_csv("Models/SKIRTOR/skirtor_2016-7-18/" + i, delim_whitespace=True, decimal=".", names= ['wl', 'TwlFwl', 'DSwlFwl', 'SSwlFwl', 'TDwlFwl', 'SDwlFwl', 'TrwlFwl'], skiprows = 7)

    c = 2.997e8
    wl = data.iloc[:, 0]*1e-6
    nu = c/wl
    nu = nu[::-1]
    log_nu = np.log10(nu)

    d = 3.086*1e22 # 10 Mpc --> m just info
    F_l = data.iloc[:, 4]/(wl*4*np.pi*d**2)
    F_nu = (F_l*wl**2)/c
    F_nu = F_nu[::-1]
    
    sep = [m.start() for m in re.finditer('_', i)]
    incl = float(i[i.find('i')+1: sep[6]])
    oa = float(i[i.find('oa')+2: sep[3]])
    tv = float(i[i.find('t')+1: sep[0]])
    p = float(i[i.find('p')+1: sep[1]])
    Md = float(DustM[DustM['model'] == i[: sep[5]]]['Mass'].values.item()[:-5])
    
    #SEDs[int(incl/10)] += F_nu/1920                              # 1 parameter
    #SEDs[int((incl*8 +oa-10)/10)] += F_nu*N_SEDs/19200           # 2 parameters
    #Mds[int((incl*8 +oa-10)/10)] += Md*N_SEDs/19200
    #SEDs[int((tv-3)/2 + ((oa-10)*5)/10 + (incl*8*5)/10)] += F_nu*N_SEDs/19200   # 3 parameters
    #Mds[int((tv-3)/2 + ((oa-10)*5)/10 + (incl*8*5)/10)] += Md*N_SEDs/19200
    SEDs[int(p*2 + (tv-3)*4/2 + ((oa-10)*4*5)/10 + (incl*4*5*8)/10)] += F_nu*N_SEDs/19200    # 4 parameters
    Mds[int(p*2 + (tv-3)*4/2 + ((oa-10)*4*5)/10 + (incl*4*5*8)/10)] += Md*N_SEDs/19200


    count += 1
    if count == 3840:
        print('20$\%$ of the finished process...')
    elif count == 7680:
        print('40$\%$ of the finished process...')
    elif count == 11520:
        print('60$\%$ of the finished process...')
    elif count == 15360:
        print('80$\%$ of the finished process...')
    elif count == 19199:
        print('Completed process.')


for j in range(N_SEDs): 
    #New_row = {'SED': SEDs[j], 'wavelength': log_nu, 'incl-values': float(j*10), 'Dm-values': Mds[j]} 
    #int_part, dec_part = divmod(j, 8)
    #New_row = {'SED': SEDs[j], 'wavelength': log_nu, 'incl-values': float(int_part*10), 'oa-values': float(dec_part*10+10),'Dm-values': Mds[j]} 
    #int_part5, dec_part5 = divmod(j, 5)
    #int_part8, dec_part8 = divmod(int_part5 , 8)
    #New_row = {'SED': SEDs[j], 'wavelength': log_nu, 'incl-values': float(int_part8*10), 'oa-values': float(dec_part8*10+10), 'tv-values': float(dec_part5*2 +3), 'Dm-values': Mds[j]} 

    int_part4, dec_part4 = divmod(j, 4)
    int_part5, dec_part5 = divmod(int_part4, 5)
    int_part8, dec_part8 = divmod(int_part5 , 8)
    New_row = {'SED': SEDs[j], 'wavelength': log_nu, 'incl-values': float(int_part8*10), 'oa-values': float(dec_part8*10+10), 'tv-values': float(dec_part5*2 +3), 'p-values': float(dec_part4/2), 'Dm-values': Mds[j]} 
    SKIRTOR = SKIRTOR.append(New_row, ignore_index = True) 


# In[ ]:


f2 = open('Models/SKIRTOR_mean_4p.pickle', 'wb')
pickle.dump(SKIRTOR, f2, protocol=2)
f2.close()

