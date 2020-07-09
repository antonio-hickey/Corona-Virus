#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 02:53:31 2020

@author: Antonio Hickey
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd
import datetime
import csv
#--------------------------------------------------------------------------------------------
# Data Mining
url =  'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html' # Target url
uClient = uReq(url) # Requesting target url
page_soup = soup(uClient.read(), "html.parser") # Reading html data of target site
uClient.close() # Close Soup
#--------------------------------------------------------------------------------------------------------
# Defining Target Data
Target_Data = page_soup.findAll("span", {"class" : "count"})
#------------------------------------------------------------------------------------------------------------
# Defining variables
Cases = Target_Data[0].text # x Daily Cases
Deaths = Target_Data[1].text # x Daily Deaths
#------------------------------------------------------------------------------------------------------------------------
# Defining x date
date_string = datetime.datetime.now().strftime("%Y-%m-%d")
#------------------------------------------------------------------------------------------------------------------------------
# Shapping Dataset
Data = (date_string, Cases, Deaths) # 1,2,3
                                    # 4,5,6
#-----------------------------------------------------------------------------------------------------------------------------
# Appending Dataset with New Elements
with open(r'/home/sratus/Desktop/Data_Science/COVID-19/Daily Cases-Deaths (CDC)/data.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(Data)
#----------------------------------------------------------------------------------------------------------------------
