import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
urls = pd.read_csv('Tunned url.csv')
all_urls = urls['URL']
dataset = pd.DataFrame(columns=['Author', 'Review', 'Profession', 'Date', 'NumberOfStars','Outlet Name',' Town', 'Street', 'ZIP code','BUNO', 'Division'])

count = 0
for item in all_urls:
    print(count+1, '/' , len(all_urls), 'URL')
    
    browser.get(item)
    showMoreButton = browser.find_elements_by_class_name("orgpage-reviews-view__more")
    showMoreButton[0].click()
    
    while len(showMoreButton):
        try: 
            showMoreButton = browser.find_elements_by_class_name("orgpage-reviews-view__more")
            showMoreButton[0].click()    
        except Exception as e:
            print("Clicking on 'Show More'")
            time.sleep(1)
    reviews = browser.find_elements_by_class_name("orgpage-reviews-view__review")
    

    i = 0
    for element in reviews:
        i = i+1
       
        text=''
        textElement = element.find_elements_by_class_name("business-review-view__body-text")
        if len(textElement) >= 1:
            text = textElement[0].text.replace('\n', '')
            
        name = ''
        nameElement = element.find_elements_by_css_selector("span")
        if len(nameElement) >= 1:
            name = nameElement[0].text
        
        profession = ''
        professionElement = element.find_elements_by_class_name("business-review-view__author-profession")
        if len(professionElement) >= 1:
            profession = professionElement[0].text
            
        date = ''
        dateElement = element.find_elements_by_class_name("business-review-view__date")
        if len(dateElement) >= 1:
            date = dateElement[0].text
            
        starsElement = element.find_elements_by_class_name("business-rating-badge-view__stars")    
        numberOfStars = 0
        if len(starsElement) >= 1:
            numberOfStars = 5 - len(starsElement[0].find_elements_by_class_name("_empty"))
        
        dataset = dataset.append({'Author': name, 'Review': text, 'Profession': profession, 'Date': date ,'NumberOfStars':numberOfStars,'Outlet Name': urls['Outlet Name'].iloc[count],' Town' : urls['Town'].iloc[count], 'Street': urls['Street'].iloc[count], 'ZIP code': urls['ZIP code'].iloc[count],'BUNO': urls['BUNO'].iloc[count], 'Division': urls['Division'].iloc[count] }, ignore_index=True)    
        print(i,'/',len(reviews),'review')
    count = count + 1

dataset.to_csv('Full Reviews.csv', index = False)