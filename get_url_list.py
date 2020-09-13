
import os


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup

def boot():
    profile = webdriver.FirefoxProfile() # add firefox settings
    profile.set_preference("dom.webnotifications.enabled", False) # close firefox notifications
    profile.update_preferences() # update firefox preferences if needed
    driver = webdriver.Firefox(firefox_profile=profile)
    return driver

def get_all_url(driver):
    #downloads the latest posts' url
    driver.get('https://theinitium.com/channel/feature/')
    moving = True
    sleep(3)

    for i in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(4) # 等待4秒鐘讓頁面讀取
        
        
    first_html = driver.page_source
    driver.close()

    soup = BeautifulSoup(first_html, 'lxml')
    #print(soup.prettify())

    url_tag = soup.find_all('a', class_='u-linkUnderline')
    #find all url tags
    url_list = []
    #to store all urls 
    for i in range(len(url_tag)):
        url_temp = url_tag[i].get('href')
        if url_temp[:5] != 'https':
            url_temp = 'https://theinitium.com' + url_temp
        url_list.append(url_temp)
        #concatenate urls

    for i in range(len(url_list)):
        print(url_list[i])

    fout = open('url_list', 'w')
    for i in range(len(url_list)):
        fout.write(str(url_list[i]))
        fout.write('\n')

driver = boot()
get_all_url(driver)