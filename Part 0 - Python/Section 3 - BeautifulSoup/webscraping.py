import requests
import pandas as pd
from bs4 import BeautifulSoup

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
data = pd.DataFrame({'Headline' : ['kjj'], 'Summary' : ['kkk'], 'Youtube link' : ['kkk']})
#print(soup.prettify())    

for article in soup.find_all('article'):
    headline = article.h2.a.text
    summary = article.find('div', class_ = 'entry-content').p.text
    try:
        vid_src = article.find('iframe', class_ = 'youtube-player')['src']
        vid_id = vid_src.split('/')[4].split('?')[0]
        yt_link = 'https://youtube.com/watch?v=' + vid_id
    except Exception as e:
        yt_link = None    
    data = data.append({'Headline': headline, 'Summary': summary, 'Youtube link': yt_link}, ignore_index=True)   
    