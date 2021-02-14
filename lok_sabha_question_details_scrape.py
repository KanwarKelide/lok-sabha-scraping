# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 23:45:03 2021

@author: KANWAR KELIDE
"""
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


#chromeDriver = "C:\\Users\\KANWAR KELIDE\\Downloads\\chromedriver"
#driver = webdriver.Chrome(chromeDriver)

all_QNumbers = []
all_QTypes   = []
all_subject  = []
all_dates    = []
all_member   = []
all_ministry = []

path = 'Desktop'
url = 'http://loksabhaph.nic.in/Questions/Qtextsearch.aspx'
#url = driver.get('http://loksabhaph.nic.in/Questions/Qtextsearch.aspx') 

#for k in range(12):

    #if k%5==0:
        #print(k)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')     
        #print (soup)

QNumber_tag = soup.find("table", {"id": "ContentPlaceHolder1_tblMember"})

QNumbers = QNumber_tag.text.strip()
print(QNumber_tag)


'''
QType_tag = soup.find("a", {"id": "ContentPlaceHolder1_rptdisplay_hyperqtype1_0"})
Qtypes = QType_tag.text.strip()


date_tag = soup.find("a", {"id": "ContentPlaceHolder1_rptdisplay_hyperdate1_0"})
dates = date_tag.text.strip()

ministry_tag = soup.find("a", {"id": "ContentPlaceHolder1_rptdisplay_hypermin1_0"})
ministry = ministry_tag.text.strip()


member_tag = soup.find("a", {"id": "ContentPlaceHolder1_rptdisplay_hypermem1_0"})
member_name = member_tag.text.strip()


subject_tag = soup.find("a", {"id": "ContentPlaceHolder1_rptdisplay_hyperhead1_0"})
subject = subject_tag.text.strip()

all_QNumbers.append(QNumbers) 
all_QTypes.append(Qtypes)
all_dates.append(dates)
all_ministry.append(ministry)
all_member.append(member_name)
all_subject.append(subject)    

ContentPlaceHolder1_tblMember

outdf = pd.DataFrame({'Question Number': all_QNumbers,
                      'Question Type': all_QTypes,
                      'Date': all_dates,
                      'Ministry': all_ministry,
                      'Member Name': all_member,
                      'Subject': all_subject})
outdf.to_csv(path + '_lok_sabha_Question.csv', index=False)          

        #element = driver.find_element_by_id("ContentPlaceHolder1_cmdNext")
        #element.click()
        '''