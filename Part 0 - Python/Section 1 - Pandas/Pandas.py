#Loading data
import pandas as pd
dataset = pd.read_csv('pokemon_data.csv')
dataset_xlxs = pd.read_excel('pokemon_data.xlsx')

#print specific data of the dataframe
print(dataset.head(5))
print(dataset.columns)
print(dataset['Name'][0:5])
print(dataset[['Name', 'HP']][0:5])
print(dataset.iloc[0:10,1:3])
for index, row in dataset.iterrows():
    print(index, row['Name'])
dataset.loc[dataset['Type 1'] == 'Fire']

#Sorting the dataframe
dataset.describe()
dataset.sort_values('Name', ascending = False)
dataset.sort_values(['Name', 'HP']) 

#Making changes to dataset
dataset['Total'] = dataset['HP'] + dataset['Attack'] + dataset['Defense']
dataset['Total'] = dataset.iloc[:, 4:9].sum(axis = 1)
dataset = dataset.drop(columns =['Total'])
dataset.to_csv('modified.csv', index = False)

#Filtering data
new_dataset = dataset.loc[(dataset['Type 1'] == 'Grass') & (dataset['Type 2'] == 'Poison')]
new_dataset = new_dataset.reset_index(drop = True, inplace = True)
dataset.loc[~dataset['Name'].str.contains('Mega')]

import re
dataset.loc[dataset['Type 1'].str.contains('fire|grass', flags = re.I, regex = True)]
dataset.loc[dataset['Name'].str.contains('^pi[a z]*', flags = re.I, regex = True)]


#Conditional changes
dataset.loc[dataset['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
dataset.loc[dataset['Type 1'] == 'Fire', 'Legendary'] = True

#Aggregate Statistics
dataset.groupby(['Type 1']).mean().sort_values('Defense')
dataset.groupby(['Type 1']).sum()
dataset['count'] = 1
dataset.groupby(['Type 1', 'Type 2']).count()['count']

#Working with large data
new_ds = pd.DataFrame(columns = dataset.columns)
for df in pd.read_csv('pokemon_data.csv', chunksize = 5):
    results = df.groupby(['Type 1']).mean()
    new_ds = pd.concat([new_ds, results])
    
