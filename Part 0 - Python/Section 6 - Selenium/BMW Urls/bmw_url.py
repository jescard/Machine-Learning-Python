import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

delay = 20

browser = webdriver.Chrome()

dataset = pd.read_excel('data.xlsm')
dataset = dataset.drop(dataset.index[[0,1,2]])
urls = pd.DataFrame(columns=['Outlet Name', 'Town', 'Street', 'ZIP code','URL'])

dataset['searchKey'] = 'BMW' +' '+ dataset.iloc[:, 15] +' '+ dataset.iloc[:, 19] +' '+ dataset.iloc[:, 22] +' '+ dataset.iloc[:, 21]

i = 0
for item in dataset['searchKey']:
    try:
        browser.get('https://yandex.ru/maps/')
        searchBar = browser.find_elements_by_class_name('input__control')[0]
        searchBar.send_keys(dataset['searchKey'].iloc[i])
        searchBar.send_keys(Keys.ENTER)
        link = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'link-wrapper'))).get_attribute('href')
        urls = urls.append({'Outlet Name': dataset.iloc[i, 15], 'Town': dataset.iloc[i, 22], 'Street': dataset.iloc[i, 19] ,'ZIP code':dataset.iloc[i, 21],'URL': link }, ignore_index=True)
       
        print (i)
    except Exception as e:
        print("Handling errors")
        
    i=i+1
    
urls.to_csv('urls.csv', index = False)

#url = pd.read_csv('urls.csv')
#datatmp = dataset.iloc[:,[15,22,19,21,33,34,35]]
#
#
#new_data = pd.DataFrame(columns=['BUNO', 'Division'])
#
#
#
#
#for i in range(0,78): 
#    bunno =  '' if pd.isnull(dataset.iloc[i,33]) else dataset.iloc[i,33]   , '' if pd.isnull(dataset.iloc[i,34]) else dataset.iloc[i,34] , '' if pd.isnull(dataset.iloc[i,35]) else dataset.iloc[i,35] ,'' if pd.isnull(dataset.iloc[i,36]) else dataset.iloc[i,36] ,'' if pd.isnull(dataset.iloc[i,37]) else dataset.iloc[i,37], '' if pd.isnull(dataset.iloc[i,38]) else dataset.iloc[i,38] 
#    bunnoStr =   ' '.join(map(str,bunno))
#    bunnoStr = bunnoStr.split(' ')
#    bunnoStr = list(set(bunnoStr))
#    bunnoStr = list(filter(None, bunnoStr))
#    bunnoStr = ' '.join(map(str,bunnoStr)) 
#    
#    division = '' if pd.isnull(dataset.iloc[i,40]) else 'BMW'   , '' if pd.isnull(dataset.iloc[i,41]) else 'MINI' , '' if pd.isnull(dataset.iloc[i,42]) else 'BMWI' ,'' if pd.isnull(dataset.iloc[i,43]) else 'RR','' if pd.isnull(dataset.iloc[i,44]) else 'MR', '' if pd.isnull(dataset.iloc[i,45]) else 'C1'
#    divisioStr =   ' '.join(map(str,division))
#    divisioStr = divisioStr.split(' ')
#    divisioStr = list(set(divisioStr))
#    divisioStr = list(filter(None, divisioStr))
#    divisioStr = ' '.join(map(str,divisioStr)) 
#    
#    new_data = new_data.append({'BUNO': bunnoStr , 'Division': divisioStr }, ignore_index=True)  
#    
#    
#new_data = new_data.drop(new_data.index[[6,28,29,71,72]])
#url = url.drop(url.index[[75,74,73]])
#new_data.to_csv('new_data.csv', index = False)
#new_data = pd.read_csv('new_data.csv')
#final_data = pd.concat([url,new_data], axis=1)

#final_data.to_csv('Tunned url.csv')