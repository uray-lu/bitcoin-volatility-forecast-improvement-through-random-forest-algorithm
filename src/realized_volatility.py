#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:00:23 2022

@author: ray
"""

import pandas as pd
import numpy as np
import os
from colorama import Back, init


init(autoreset = True)

def realized_volatility(data):
    
    data  = pd.read_csv(data)    
    data['Return'] = (np.log(data.close/data.close.shift(1)))
    data['Return'] = data['Return'] **2
    
    
    for i in range(len(data['date'])):
        data['date'][i] = str(data['date'][i])
        data['date'][i] = data['date'][i][:10]
        
    df = data[['date', 'Return']]
    
    volatility = df.groupby(df['date']).sum()
    volatility = pd.DataFrame(volatility)
    volatility = volatility.rename({'Return' : 'RV' }, axis = 1)
    volatility = volatility.reset_index()
    volatility = volatility.drop(0).reset_index(drop = True)
    
    root_path = os.getcwd()[:os.getcwd().find('/bitcoin-volatility-forecast-improvement-through-random-forest-algorithm')+len('bitcoin-volatility-forecast-improvement-through-random-forest-algorithm/')]
    

    
    volatility.to_csv(root_path+'/data/processed/btc_info/Realized_volatility_unit(d).csv')
    print(f"{'Realized Volatility calculation': <10}{'.'*20 :^10}{Back.GREEN}{'pass': ^10}")
    

realized_volatility('./data/raw/btc_info/Hourly_kline.csv')







