# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 10:57:25 2018

@author: Akhila Sri Manasa
"""

import requests
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://stackoverflow.com/')
soup = BeautifulSoup(page.text, 'html.parser')


question_name_list = soup.find(class_='question-hyperlink')


question_name_list_items = question_name_list.find_all('a')

for question_name in question_name_list_items:
    
    output = question_name.prettify()
    file = open("sampleNew.txt","a")
    file.write(output)
    file.close
    print(output)        

