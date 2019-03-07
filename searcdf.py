"""
Created on Mon Dec 31 10:41:38 2018
"""
#importing pandas library
import pandas as pd

#reading csv file
df = pd.read_csv('ecommerce_data.csv')

#accessing the required data column using iloc function
#working of iloc:
#.iloc[index of starting row : index of ending row+1, index of starting column: index of ending column+1] 
var1 = df.iloc[0:,2:3].values

count = 0
#couting number of values in the required range
for var in var1:
    if var > 0.5 and var < 0.6:
        count = count + 1
print(count)
