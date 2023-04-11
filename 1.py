#%%
from ast import Try
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
from selenium.webdriver.common.by import By
import json
import re
import csv
#%%
def store_location():
  driver = webdriver.Chrome('./chromedriver')
  store = 'nfs-chattarpur'
  web_link = 'https://www.nike.com/in/retail/s/' + store
  driver.get(web_link)
  
  store_name = driver.find_element(By.XPATH, '//*[@id="store-page"]/article/section[1]/h1').text
  store_address = driver.find_element(By.XPATH, '//*[@id="store-page"]/article/section[1]/div[2]/div[1]').text
  store_hours = driver.find_element(By.XPATH, '//*[@id="store-page"]/article/section[1]/div[3]/section[1]').text
  store_contact = driver.find_element(By.XPATH, '//*[@id="store-page"]/article/section[1]/div[2]/p').text
  store_map_link = driver.find_element(By.XPATH, '//*[@id="store-page"]/article/section[1]/div[2]/div[2]/div[1]/a').get_attribute('href')
  lat = re.findall('=([\w\-\.]+),', store_map_link)
  long = re.findall(',([\w\-\.]+)', store_map_link)
  print(store_name)
  print(store_address)
  print(store_hours)
  print(store_contact)
  print(store_map_link)
  print(lat[0])
  print(long[0])
  row_head =['Store_Name', 'Store_Address', 'Store_hours', 'Store_contact', 'Store_latitude', 'Store_Longitude']
  Data = []
  Data.append(store_name)
  Data.append(store_address)
  Data.append(store_hours)
  Data.append(store_contact)
  Data.append(lat[0])
  Data.append(long[0])
  rows = [Data[i:i + 6] for i in range(0, len(Data), 6)]
  with open('data.csv', 'w', encoding='utf_8_sig', newline="") as csvfile:
      csvwriter = csv.writer(csvfile)
      csvwriter.writerow(row_head)
      csvwriter.writerows(rows)
#%%
import sys
store_location()
# %%
