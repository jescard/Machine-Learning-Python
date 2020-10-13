import pandas as pd
import time
import emoji
from langdetect import detect
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.google.com/travel/hotels/entity/CgoIha-XzbS0_ccrEAE/reviews?g2lb=202157%2C2502548%2C4258168%2C4260007%2C4270442%2C4274032%2C4305595%2C4306835%2C4317915%2C4328159%2C4329288%2C4364504%2C4366684%2C4367953%2C4371334%2C4373849%2C4381263%2C4385383%2C4386665%2C4390422%2C4395397%2C4395402%2C4270859%2C4284970%2C4291517%2C4316256%2C4356900&hl=en&gl=lb&un=1&rp=EIWvl820tP3HKxCFr5fNtLT9xys4AkAASAE&ictx=1&sa=X&utm_campaign=sharing&utm_medium=link&utm_source=htls&hrf=IgNMQlAqFgoHCOQPEAcYDBIHCOQPEAcYDRgBKACCASUweDg4ZTQ1NWViZDJjNWNiMzk6MHgyYjhmZjVhMzQ5YTVkNzg1mgEnGiUweDg4ZTQ1NWViZDJjNWNiMzk6MHgyYjhmZjVhMzQ5YTVkNzg1')
SCROLL_PAUSE_TIME = 0.1
# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")
new_height = last_height
body = browser.find_element_by_css_selector('body')
i = 0

while True:
    i = i+1
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(SCROLL_PAUSE_TIME)
    
    if i == 50:
        new_height = browser.execute_script("return document.body.scrollHeight")
        i=0
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(4)
        if new_height == last_height:
            break
    last_height = new_height
    

dataset = pd.DataFrame(columns=['Author', 'Review','Trip_type','Rate','Room_rate /5','Service_rate /5','Location_rate /5','Sentiment','Date_Website', 'Average_rating', 'Average_Room_rating', 'Average_Location_rating','Average_Service_rating','Average_Couple_rating', 'Average_Solo_rating', 'Average_Business_rating','Average_Families_rating'])


avg_rating = browser.find_element_by_class_name("BARtsb").text


business_rating = ''
solo_rating = ''
couple_rating = ''
families_rating = ''
room_rating = ''
location_rating = ''
service_rating = ''

other_ratings = browser.find_elements_by_class_name("w0q4db")
if(len(other_ratings)>0):
    room_rating = other_ratings[0].text
if(len(other_ratings)>1):
    location_rating = other_ratings[1].text
if(len(other_ratings)>2):
    service_rating = other_ratings[2].text


other_ratings = browser.find_elements_by_class_name("fBDixb")
if(len(other_ratings)>0):
    couple_rating = other_ratings[0].text
if(len(other_ratings)>1):
    families_rating = other_ratings[1].text
if(len(other_ratings)>2):
    solo_rating = other_ratings[2].text
if(len(other_ratings)>3):
    business_rating = other_ratings[3].text

reviews = browser.find_elements_by_class_name("Svr5cf")
text = ''
i = 0
for element in reviews:
    print(i)
    i = i+1
    single_rev = element
    textElement = single_rev.find_elements_by_class_name("K7oBsc")
    if len(textElement) > 0:
        text = textElement[0].text
#        
#    if(len(text)>3):
#        lang = dete                                    ct(text)
#    else:
#        lang = 'en'
#        
    if True:
        name = ''
        text = ''
        trip = ''
        single_room_rate = ''
        single_service_rate = ''
        single_location_rate = ''
        website = ''
        rate_single = ''

        date = ''
        sentiment = ''
        
        try:
            showMoreButton = element.find_elements_by_class_name("TJUuge")
            if len(showMoreButton) > 0:
               time.sleep(2)
               browser.execute_script("arguments[0].click();", showMoreButton[0])
               textElement = single_rev.find_elements_by_class_name("K7oBsc")
               if len(textElement) > 0:
                   text = textElement[1].text
                   text = emoji.demojize(text)
            else:
                textElement = single_rev.find_elements_by_class_name("K7oBsc")
                if len(textElement) > 0:
                    text = textElement[0].text
                    text = emoji.demojize(text)
                
        except Exception as e:
            print('sda')
    
        tripElement = single_rev.find_elements_by_class_name("m3DKsd")
        if len(tripElement) > 0:
            trip = tripElement[0].text
        rslElement = single_rev.find_elements_by_class_name("B5Raud")
        nameElement = single_rev.find_elements_by_class_name("DHIhE")
        if len(nameElement) > 0:
            name = nameElement[0].text
        nameElement = single_rev.find_elements_by_class_name("faBUBf")
        if len(nameElement) > 0:
            name = nameElement[0].text
        websiteElement = single_rev.find_elements_by_class_name("iUtr1")
        if len(websiteElement) > 0:
            website = websiteElement[0].text
        rateElement = single_rev.find_elements_by_class_name("KdvmLc")
        if len(rateElement) > 0:
            rate_single = rateElement[0].text
        
        try:
            sent = rate_single.split('/') 
          
            avgRateSent= float(sent[0]) / float(sent[1])
            if avgRateSent > 0.59:
                sentiment = 'Good'
            elif avgRateSent >0.41:
                sentiment = 'Average'
            else:
                sentiment = 'Bad'
        except Exception as e:
                print()
        
        try:
            if len(rslElement) > 0:
                single_room_rate = rslElement[0].find_elements_by_css_selector("span")[1].text
                single_service_rate = rslElement[1].find_elements_by_css_selector("span")[1].text
                single_location_rate = rslElement[2].find_elements_by_css_selector("span")[1].text
        except Exception as e:
            print()
        
        dataset = dataset.append({'Author': name, 'Review': text,'Trip_type': trip,'Rate': rate_single,'Room_rate /5': single_room_rate,'Service_rate /5': single_service_rate,'Location_rate /5': single_location_rate,'Sentiment': sentiment,'Date_Website': website, 'Average_rating': avg_rating, 'Average_Room_rating': room_rating, 'Average_Location_rating': location_rating,'Average_Service_rating': service_rating,'Average_Couple_rating': couple_rating, 'Average_Solo_rating': solo_rating, 'Average_Business_rating': business_rating,'Average_Families_rating': families_rating}, ignore_index=True)    

dataset.to_excel('The Ritz-Carlton, Amelia Island Reviews.xlsx', index = False)

