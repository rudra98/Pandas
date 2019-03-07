# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 10:41:38 2018

@author: dubek
"""
import pandas as pd

df = pd.read_csv('C:/Users/dubek/Downloads/Folder/ecommerce_data.csv')

var1 = df.iloc[0:,2:3].values
#print(var1)
count = 0
for var in var1:
    if var > 0.5 and var < 0.6:
        count = count + 1
print(count)