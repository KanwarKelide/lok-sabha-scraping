# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 00:40:26 2021

@author: KANWAR KELIDE
"""

#Code Name : lok sabha member numerics
#Source : http://loksabhaph.nic.in/Members/Memberhomepage.aspx
#Purpose : Extracting member details
#Predecessor : lok_sabha_url_scrape
#Successor : 
#Date originally writen : 03/02/2021


import requests
from bs4 import BeautifulSoup
import pandas as pd

path = "C:\\Users\\KANWAR KELIDE\\OneDrive\\Desktop\\"


all_current_debate = []
all_archive_debate = []
all_current_special_mention = []
all_archive_special_mention = []
all_current_question = []
all_archive_question = []
all_current_supplementary_question = []
all_archive_supplementary_question = []
all_current_govt_bill = []
all_archive_govt_bill = []
all_current_private_member_bill = []
all_archive_private_member_bill = []
all_current_private_member_resolution = []
all_archive_private_member_resolution = []
all_current_commitee_membership = []
all_archive_commitee_membership = []

df = pd.read_csv(path + 'Desktop_lok_sabha_page_urls.csv')
length = len(df)
#print (length)
for k in range (529):

    if k%10==0:
        print(k)

    u = df.iloc[k]['url']
    #print (u)
    page = requests.get(u)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    
    
    
#----------------------------------------DEBATES------------------------------------------      
    #current debate      
    current_debate_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_current" })
    current_debate = current_debate_tags.text.strip().split('(')[-1].split(')')[0]
    all_current_debate.append(current_debate)
   
    
    #archive debate  
    archive_debate_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_LinkButton13" })
    archive_debate = archive_debate_tags.text.strip().split(':')[1]
    all_archive_debate.append(archive_debate)
    
#------------------------------------SPECIAL MENTIONS--------------------------------------    
    
    
    #current special mention      
    current_special_mention_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_currentsm" })
    current_special_mention = current_special_mention_tags.text.strip().split('(')[-1].split(')')[0]
    all_current_special_mention.append(current_special_mention)
    
    
    #archive special mention
    archive_special_mention_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_LinkButton14" })
    archive_special_mention = archive_special_mention_tags.text.strip().split(':')[1]
    all_archive_special_mention.append(archive_special_mention) 
    

#----------------------------------------QUESTION------------------------------------------    
    
    #current question     
    current_question_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_Currentq" })
    current_question = current_question_tags.text.strip().split('(')[-1].split(')')[0]
    all_current_question.append(current_question)
    
    
    #archive question
    archive_question_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_LinkButton28" })
    archive_question = archive_question_tags.text.strip().split('(')[-1].split(')')[0]
    all_archive_question.append(archive_question)  
    

#---------------------------SUPPLEMENTARY QUESTION----------------------------------------    
    
    #current supplementary question     
    current_sup_question_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_supply_current15" })
    current_supplementary_question = current_sup_question_tags.text.strip().split('(')[-1].split(')')[0]
    all_current_supplementary_question.append(current_supplementary_question)
    
    
    #archive supplementary question
    archive_sup_question_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_LinkButton29" })
    archive_supplementary_question = archive_sup_question_tags.text.strip().split('(')[-1].split(')')[0]
    all_archive_supplementary_question.append(archive_supplementary_question)      
    
    

#---------------------------GOVERNMENT BILLS----------------------------------------    
    
    #current government bills   
    current_govt_bill_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_currentgb" })
    current_govt_bill = current_govt_bill_tags.text.strip().split('(')[-1].split(')')[0]
    all_current_govt_bill.append(current_govt_bill)
    
    
    #archive government bills
    archive_govt_bill_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_LinkButton30" })
    archive_govt_bill = archive_govt_bill_tags.text.strip().split('(')[-1].split(':')[1]
    all_archive_govt_bill.append(archive_govt_bill)      
    
    
    
#---------------------------PRIVATE MEMBER BILLS----------------------------------------    
    
    #current private member bills   
    current_private_bill_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_currentpb" })
    current_private_bill = current_private_bill_tags.text.strip().split('(')[-1].split(')')[0]
    all_current_private_member_bill.append(current_private_bill)
    
    
    #archive private member bills
    archive_private_bill_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_LinkButton31" })
    archive_private_bill = archive_private_bill_tags.text.strip().split('(')[-1].split(':')[1]
    all_archive_private_member_bill.append(archive_private_bill)      
    #print (archive_private_bill)
    
    

#---------------------------PRIVATE MEMBER RESOLUTION----------------------------------------    
    
    #current private member resolution   
    current_private_res_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_currentpmr" })
    current_private_resolution = current_private_res_tags.text.strip().split('(')[-1].split(')')[0]
    all_current_private_member_resolution.append(current_private_resolution)
   
    
    #archive private member resolution
    archive_private_res_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_LinkButton32" })
    archive_private_resolution = archive_private_res_tags.text.strip().split('(')[-1].split(':')[1]
    all_archive_private_member_resolution.append(archive_private_resolution)      
    
    

#---------------------------COMMITEE MEMBERSHIP------------------------------------------    
    
    #current commitee membership   
    current_comm_member_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_currentcmem" })
    current_commitee_membership = current_comm_member_tags.text.strip().split('(')[-1].split(')')[0]
    all_current_commitee_membership.append(current_commitee_membership)
       
    
    #archive commitee membership
    archive_comm_member_tags = soup.find("a", {"id": "ContentPlaceHolder1_MemberUC_LinkButton33" })
    archive_commitee_membership = archive_comm_member_tags.text.strip().split('(')[-1].split(')')[0]
    all_archive_commitee_membership.append(archive_commitee_membership)      
   
    
    outdf = pd.DataFrame({'Number of current debates': all_current_debate,
                      'Number of archive debates': all_archive_debate,
                      'Number of current special mention': all_current_special_mention,
                      'Number of archive special mention': all_archive_special_mention,
                      'Number of current question': all_current_question,
                      'Number of archive question': all_archive_question,
                      'Number of current supplementary question': all_current_supplementary_question,
                      'Number of archive supplementary question': all_archive_supplementary_question,
                      'Number of current government bill': all_current_govt_bill,
                      'Number of archive government bill': all_archive_govt_bill,
                      'Number of current private member bill': all_current_private_member_bill,
                      'Number of archive private member bill': all_archive_private_member_bill,
                      'Number of current private member resolution': all_current_private_member_resolution,
                      'Number of archive private member resolution': all_archive_private_member_resolution,
                      'Number of current commitee membership': all_current_commitee_membership,
                      'Number of archive commitee membership': all_archive_commitee_membership,
                      
            
                      })
    outdf.to_csv(path + '_lok_sabha_numerics.csv', index=False)

    
    
    
    