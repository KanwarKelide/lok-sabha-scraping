# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:56:56 2021

@author: KANWAR KELIDE
"""


#Code Name : lok sabha member details
#Source : http://loksabhaph.nic.in/Members/Memberhomepage.aspx
#Purpose : Extracting member details
#Predecessor :
#Successor : lok_sabha_specific_numerics.py
#Date originally writen : 03/02/2021


import requests
from bs4 import BeautifulSoup
import pandas as pd

path = 'Desktop'
URL = 'http://loksabhaph.nic.in/Members/Memberhomepage.aspx'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

all_urls = []
all_members = []

tags = soup.find("div", {"id": "ContentPlaceHolder1_UpdatePanel1"})
 #----------------------------page url / name-----------------------------------#   

for i in tags:
      j = str(i)
      if 'a' in j:
          #print (j)
          url = j.split('href="')[1].split('"')[0].strip()
          name = j.split('href="')[1].split('</a></td></tr>')[0].strip(url)
          #print(url)
          #print (name)
          all_urls.append('http://loksabhaph.nic.in/Members/'+url)     
          all_members.append(name)
          outdf = pd.DataFrame({'url': all_urls,
                                'name': all_members})
          outdf.to_csv(path + '_lok_sabha_page_urls.csv', index=False)


