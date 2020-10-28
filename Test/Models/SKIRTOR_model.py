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


column_names = ["wavelength", 'SED', 'tv-values', 'p-values', 'q-values', 'oa-values', 'r-values', 'mcl-values', 'incl-values', 'Dm-values']  #To create the columns of the dataframe
SKIRTOR = pd.DataFrame(columns = column_names)
DustM = pd.read_csv("Models/SKIRTOR/total_dust_mass_2016-7-18.txt", sep = '    ', decimal=".", names= ['model', 'Mass'], skiprows = 2, engine = 'python')
j = 0

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
    tv = float(i[i.find('t')+1: sep[0]])
    p = float(i[i.find('p')+1: sep[1]])
    q = float(i[i.find('q')+1: sep[2]])
    oa = float(i[i.find('oa')+2: sep[3]])
    r = float(i[i.find('R')+1: sep[4]])
    mcl = float(i[i.find('Mcl')+3: sep[5]])
    incl = float(i[i.find('i')+1: sep[6]])
    Md = float(DustM[DustM['model'] == i[: sep[5]]]['Mass'].values.item()[:-5])
    
    New_row = {'SED': F_nu, 'wavelength': log_nu, 'tv-values': tv, 'p-values': p, 'q-values': q, 'oa-values': oa, 'r-values': r, 'mcl-values': mcl, 'incl-values': incl, 'Dm-values': Md} 
    SKIRTOR = SKIRTOR.append(New_row, ignore_index = True) 
    j += 1
    if j == 3840:
        print('20$% of the finished process...')
    elif j == 7680:
        print('40$% of the finished process...')
    elif j == 11520:
        print('60$% of the finished process...')
    elif j == 15360:
        print('80$% of the finished process...')
    elif j == 19199:
        print('Completed process.')


# In[ ]:


f2 = open('Models/SKIRTOR.pickle', 'wb')
pickle.dump(SKIRTOR, f2, protocol=2)
f2.close()

