import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('https://yandex.ru/maps/org/avtodom_bmw/1037910515/?ll=37.508706%2C55.786389&utm_source=geoblock_maps_moscow&z=10')
showMoreButton = browser.find_elements_by_class_name("orgpage-reviews-view__more")
showMoreButton[0].click()

while len(showMoreButton):
    try: 
        showMoreButton = browser.find_elements_by_class_name("orgpage-reviews-view__more")
        showMoreButton[0].click()    
    except Exception as e:
        print("error")
        time.sleep(1)
        
reviews = browser.find_elements_by_class_name("orgpage-reviews-view__review")

dataset = pd.DataFrame(columns=['Author', 'Review', 'Profession', 'Date', 'NumberOfStars'])
i = 0
for element in reviews:
    i = i+1
    text = element.find_elements_by_class_name("business-review-view__body-text")[0].text.replace('\n', '')
    name = element.find_elements_by_css_selector("span")[0].text
    profession = element.find_elements_by_class_name("business-review-view__author-profession")[0].text
    date = element.find_elements_by_class_name("business-review-view__date")[0].text
    starsElement = element.find_elements_by_class_name("business-rating-badge-view__stars")
    if len(starsElement) == 1:
        numberOfStars = 5 - len(starsElement[0].find_elements_by_class_name("_empty"))
    dataset = dataset.append({'Author': name, 'Review': text, 'Profession': profession, 'Date': date ,'NumberOfStars':numberOfStars }, ignore_index=True)    
    print(i)

dataset.to_csv('Reviews.csv', index = False)