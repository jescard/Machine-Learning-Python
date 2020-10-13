from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.seleniumhq.org/')
elem = browser.find_element_by_link_text('Downloads')
print(elem.text)
print(elem.get_attribute('href'))
elem.click()

searchBar = browser.find_element_by_id('gsc-i-id1')
searchBar.send_keys('downloads')
searchBar.send_keys(Keys.ENTER)