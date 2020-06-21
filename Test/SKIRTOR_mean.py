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
j = 0

SEDs = [np.zeros((132))]*10
Mds = np.zeros((10))

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
    Md = float(DustM[DustM['model'] == i[: sep[5]]]['Mass'].values.item()[:-5])
    
    SEDs[int(incl/10)] += F_nu/1920
    Mds[int(incl/10)] += Md/1920

for j in range(10):
    New_row = {'SED': SEDs[j], 'wavelength': log_nu, 'incl-values': float(j*10), 'Dm-values': Mds[j]} 
    SKIRTOR = SKIRTOR.append(New_row, ignore_index = True) 


# In[ ]:


f2 = open('Models/SKIRTOR_mean.pickle', 'wb')
pickle.dump(SKIRTOR, f2, protocol=2)
f2.close()

