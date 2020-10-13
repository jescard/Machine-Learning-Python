# -*- coding: utf-8 -*-
import os
import pandas as pd

#Merging all 12 months in one big file
all_months_data = pd.DataFrame()
files = [file for file in os.listdir('./sales_data')]
for file in files:
    dataset = pd.read_csv('./sales_data/' + file)
    all_months_data = pd.concat([all_months_data, dataset])

all_months_data.to_csv('all_data.csv', index = False)

#reading all data
dataset = pd.read_csv('all_data.csv')

#Question 1: What was the best month for sales? How much was earned that month

#Augment data with aditional columns

#Clean up the data
#Drop rows of NaN
nan_df = dataset[dataset.isna().any(axis = 1)]
dataset = dataset.dropna(how = 'all')

#Find Or data and delete it
temp = dataset[dataset['Order Date'].str[0:2] == 'Or']
dataset = dataset[dataset['Order Date'].str[0:2] != 'Or'] 

#Add month column 
dataset['Month'] = dataset['Order Date'].str[0:2]
dataset['Month'] = dataset['Month'].astype('int32')

#Convert Column to the correct type
dataset['Quantity Ordered'] = pd.to_numeric(dataset['Quantity Ordered'])
dataset['Price Each'] = pd.to_numeric(dataset['Price Each'])

#Add a sales column
dataset['Sales'] = dataset['Quantity Ordered'] * dataset['Price Each']

#Getting the best sale month
results = dataset.groupby('Month').sum()

import matplotlib.pyplot as plt
months = range(1,13)
plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in $')
plt.xlabel('Months')
plt.show()


#Question 2: What city has the most number of sales
#Add city column
def get_city(address):
    return address.split(',')[1]
def get_state(address):
    return address.split(',')[2].split(' ')[1]

dataset['City'] = dataset['Purchase Address'].apply(lambda x: get_city(x) + ' (' + get_state(x) + ')')
results2 = dataset.groupby('City').sum()

plt.bar(results2.index, results2['Sales'])
plt.xticks(results2.index, rotation = 'vertical')
plt.ylabel('Sales in $')
plt.xlabel('City')
plt.show()

#Question 3: What time should we display advertisments to maximize likelihood of customer's buying product?
dataset['Order Date'] = pd.to_datetime(dataset['Order Date'])
dataset['Hour'] = dataset['Order Date'].dt.hour
results3 = dataset.groupby('Hour').count()
plt.plot(results3.index, results3['Product'])
plt.grid()
plt.xticks(results3.index)
plt.show()

