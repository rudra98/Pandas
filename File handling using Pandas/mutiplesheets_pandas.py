#Importing necessary libraries
import pandas as pd

#reading the file using pandas
df = pd.read_csv('olist_sellers_dataset.csv')

#copy columns to work in different dataframe
df1 = df[['seller_id','seller_zip_code_prefix']].copy()

#checking values/perform operations
zipcodes = []
for value in df1['seller_zip_code_prefix'].values:
    if value > 47000 and value < 58000:
        zipcodes.append(value)

#loc for accessing particular column
#isin to check that it is in zipcodes or not        
var = df1.loc[df1['seller_zip_code_prefix'].isin(zipcodes)]

#to make a sorted dataframe
selectedids = var[['seller_id']].copy()



#accessing another file to work on both dataframes
df2 = pd.read_csv('olist_order_items_dataset.csv')
otherdf = df2[['seller_id','order_item_id','price']].copy()

#checking the condition
final = otherdf.loc[otherdf['seller_id'].isin(selectedids)]