from selenium import webdriver
from bs4 import BeautifulSoup
import requests as r
import time
import csv
import pandas as pd

Start_Url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(Start_Url)
time.sleep(10)

soup = BeautifulSoup(browser.page_source,"html.parser")
data  = []
header = ["star_name","distance","radius","mass"]
Div = soup.find_all("table")
table_rows = Div[3].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text.rstrip() for tr in td]
    data.append(row)

star_name = []
distance = []
radius = []
mass = []
for i in range(1,len(data)):
    star_name.append(data[i][0])
    distance.append(data[i][5])
    radius.append(data[i][9])
    mass.append(data[i][8])

df = pd.DataFrame(list(zip(star_name,distance,radius,mass,)),columns=['Star_name','Distance','Mass','Radius'])

df.to_csv('project128.csv')
