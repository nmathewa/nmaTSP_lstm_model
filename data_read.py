#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 13:40:57 20200
NMA model train sessions
@author: nma
"""

#importing all libraries
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, Bidirectional

#weather data in CSV format
dataset = "/media/nma/EDU/python/AI'/Weather/mpi_roof.csv"
#setting the dateparse function with the format(a dateformat should be needed in the input CSV)
dateparse = lambda x: dt.datetime.strptime(x, '%d.%m.%Y %H:%M:%S')


#reading the csv data,setting the parse date
dft_all = pd.read_csv(dataset,engine='python',parse_dates=['Date Time'], date_parser=dateparse)

#making it hourly [start:stop:step]
dft = dft_all[5::6]

#extracting the date column for later use
date_time = dft.pop("Date Time")

#des = dft.describe().transpose()

#%% data processing

#%%Feature engineering

#sample plotting
plot_cols = ['T (degC)', 'p (mbar)', 'rho (g/m**3)']
plot_features = dft[plot_cols]
#setting the date_time as index
plot_features.index = date_time

#plot_features.plot(subplots=True)

plot_features = dft[plot_cols][:200]
plot_features.index = date_time[:200]

plot_features.plot(subplots=True)

#%% wind pro

wv = dft['wv (m/s)']

#converting dire to radians
wd_rad = dft.pop('wd (deg)')*np.pi/180

##Calculating u and v
dft["Wx"] = wv*np.cos(wd_rad)
dft["Wy"] = wv*np.sin(wd_rad) 

## max wind x and y components
#%%
plt.hist2d(dft['Wx'], dft['Wy'], bins=(50, 50), vmax=50)
plt.colorbar()
plt.xlabel('Wind X [m/s]')
plt.ylabel('Wind Y [m/s]')
ax = plt.gca()
ax.axis('tight')

#%% periodicity in data

timestamp_s = date_time.map(dt.datetime.timestamp)

# converting the periodicity in to sin and cos time of day and time of year signals

day = 24*60*60
year = (365.2425)*day

dft["Day sin"] = np.sin(timestamp_s*(2*np.pi/day))
dft["Day cos"] = np.cos(timestamp_s*(2*np.pi/day))
dft["Year sin"] = np.sin(timestamp_s*(2*np.pi/day))
dft["Year cos"] = np.cos(timestamp_s*(2*np.pi/day))


plt.plot(np.array(dft["Day sin"])[:25])
plt.plot(np.array(dft["Day cos"])[:25])