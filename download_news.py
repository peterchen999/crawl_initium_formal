import os
import requests
import re

import selenium
from time import sleep
from bs4 import BeautifulSoup

url_file = open('url_list', 'r')
url_list = url_file.readlines()
url_file.close()

for i in range(len(url_list)):
    url_list[i].strip()
    print(url_list[i])

for i in range(len(url_list)):
    try:
        r = requests.get(url_list[i])
        soup = BeautifulSoup(r.text, 'lxml')
        news_title = soup.find('h1', class_='p-article__title').text
        news_subtitle = soup.find('p', class_='p-article__lead u-font-sans').text
        news_content_paragraph_tag_list = soup.find('div', class_=re.compile('p-article__content u-content')).find_all('p')
        news_content_paragraph_list = []

        for k in range(len(news_content_paragraph_tag_list)):
            news_content_paragraph_list.append(news_content_paragraph_tag_list[k].text)
        print(news_title)
        print(news_subtitle)

        for k in range(len(news_content_paragraph_list)):
            print(news_content_paragraph_list[k])

        fout = open('news/'+news_title, 'w')
        fout.write(news_title)
        fout.write(news_subtitle)
        for k in range(len(news_content_paragraph_list)):
            fout.write(news_content_paragraph_list[k])
        fout.close()
    except:
        print('error, check if its project')
        print(news_title)
        input('waiting')

