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
N_SEDs = 80 #10 incl, 80 incl+oa
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
    Md = float(DustM[DustM['model'] == i[: sep[5]]]['Mass'].values.item()[:-5])
    
    #SEDs[int(incl/10)] += F_nu/1920
    SEDs[int((incl*8 +oa-10)/10)] += F_nu*N_SEDs/19200
    Mds[int((incl*8 +oa-10)/10)] += Md*N_SEDs/19200

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
    int_part, dec_part = divmod(j, 8)
    New_row = {'SED': SEDs[j], 'wavelength': log_nu, 'incl-values': float(int_part*10), 'oa-values': float(dec_part*10+10),'Dm-values': Mds[j]} 
    SKIRTOR = SKIRTOR.append(New_row, ignore_index = True) 


# In[ ]:


f2 = open('Models/SKIRTOR_mean_2p.pickle', 'wb')
pickle.dump(SKIRTOR, f2, protocol=2)
f2.close()

