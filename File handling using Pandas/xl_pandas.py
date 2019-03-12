#importing important libraries
import pandas

#loading the file in program
df = pandas.read_csv('xl_pandas.csv', header=None)

#using .iloc function to access dataframe
#accessing iloc[0throw to last row, 0th column to 1st column excluding]
var1 = df.iloc[0:,0:1]
print(var1)

#[0th row:last row, 2nd column: 3rd column excluding]
var2 = df.iloc[0:,2:3]
var1['1'] = var2

#[0th row: 5th row excluding, 1st column:2nd column excluding]
var3 = df.iloc[0:5,1:2]
var1['2'] = var3

#accesing particular column, rows and cells
var4 = df.iloc[0:,3:4]
var5 = df.iloc[0:,4:5]
var6 = df.iloc[0:,5:]

#accessing using label name
var1['3'] = var4
var1['4'] = var5
var1['5'] = var6

df = var1
print(df)