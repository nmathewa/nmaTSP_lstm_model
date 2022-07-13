#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 10:49:34 2022

@author: nma
"""
import pandas as pd ; import numpy as np
import glob ; import re
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

    def read_logger(self):
        wd_files = glob.glob(self.in_dir + "*.wnd")
        def read_wnd(file):
            dft = pd.read_csv(file,skiprows=3,sep=';',decimal=',',thousands='.',parse_dates=[0])
            return dft
        raw_dft = pd.concat(map(read_wnd,wd_files)).iloc[:,:-1].set_index("DateTime")
        
        
        def rename_lab(raw_data):
            
            colss = list(raw_data.columns)
            wea_var = {'WS','WD','TEM','RH','PR','RAD'}
            
            val_cols = [cols for cols in colss if "-" not in cols]
            
            cols_f = []
            n_cols = {}
            for ii in wea_var:
                cols_f += [cols for cols in val_cols if ii in cols]

            for jj in cols_f:
                n_name = jj.split('_')
                if n_name[1] == 'WS':
                    n_cols[jj] = n_name[1] + n_name[2] +'_'+ n_name[3]
                else :
                    n_cols[jj] = n_name[1] + n_name[2]
            
            n_data = raw_data.rename(columns = n_cols)[n_cols.values()]
            return n_data
        n_dft = rename_lab(raw_dft)
        return n_dft
    
    
    
    def read_custom(self):
        pass
                         
dd = data_pro("/home/nma/dev/","/home/nma/dev/outs/")


dtt = dd.gen_rts('10-01-2020','11-01-2020',['T','P','WS'])




k_data = dd.read_logger()

#%%


k_data['WS100_120'].plot()
        
