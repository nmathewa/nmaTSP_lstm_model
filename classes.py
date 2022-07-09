#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 10:49:34 2022

@author: nma
"""
import pandas as pd ; import numpy as np
import glob
#%%


class data_pro:
    
    def __init__(self,in_dir,out_dir):
        self.in_dir = in_dir
        self.out_dir = out_dir        
       
   
    def gen_rts(self,start_time,end_time,variables):
        dt = pd.date_range(start_time,end_time,freq='10min')
        var_dict = {}
        for ii in variables :
            if ii == 'T':
                temp = pd.Series(np.random.randint(12,32,size=len(dt)),
                                 name='temp')
                var_dict['temp'] = temp
                
            if ii == 'P':
                pres = pd.Series(np.random.randint(12,32,size=len(dt)),
                                 name='pres')
                var_dict['pres'] = pres
                
            if ii == 'H':
                hum = pd.Series(np.random.randint(12,32,size=len(dt)),
                                 name='hum')
                var_dict['hum'] = hum
                
            if ii == 'WS':
                ws = pd.Series(np.random.randint(12,32,size=len(dt)),
                                 name='ws')
                var_dict['ws'] = ws
                
            if ii == 'WD':
                wd = pd.Series(np.random.randint(12,32,size=len(dt)),
                                 name='wd')
                var_dict['WD'] = wd
                
        dft = pd.concat(var_dict,axis=1).set_index(dt)
            
        return dft

    def read_kintech(self):
        wd_files = glob.glob(self.in_dir + "*.wnd")
        def read_wnd(file):
            dft = pd.read_csv(file,skiprows=3,sep=';',decimal=',',thousands='.',parse_dates=[0])
            return dft
        n_dft = pd.concat(map(read_wnd,wd_files)).iloc[:,:-1]
        return n_dft
    
    
    
    def read_custom(self):
        pass
                         
dd = data_pro("/home/nma/dev/","/home/nma/dev/outs/")


dtt = dd.gen_rts('10-01-2020','11-01-2020',['T','P','WS'])



colss = k_data.columns

k_data = dd.read_kintech()


        
        
        
        
        
        
        
