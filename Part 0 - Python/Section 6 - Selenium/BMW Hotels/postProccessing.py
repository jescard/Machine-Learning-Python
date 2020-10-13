# -*- coding: utf-8 -*-

import pandas as pd
import time
from langdetect import detect
import math

dataset = pd.read_excel('The Ritz-Carlton, Amelia Island Reviews.xlsx')

db = pd.DataFrame(columns=['index'])


i = 0
for element in dataset['Review']:
    if not pd.isna(element):       
        if "(Translated by Google)" in element:
            print(i)
            db = db.append({'index': i},ignore_index=True)
            
        elif detect(element) != 'en':
            db = db.append({'index': i},ignore_index=True)
    i=i+1
    
dataset = dataset.drop(db['index'])

dataset.to_excel('The Ritz-Carlton, Amelia Island Reviews(English Only).xlsx', index = False)
