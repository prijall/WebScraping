import requests
from bs4 import BeautifulSoup
import re

url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
r=requests.get(url)

soup=BeautifulSoup(r.text, 'lxml')

#for data
data=soup.find_all(['h4', 'a', 'p'])
print(data)

#to see all  of 'Galaxy Tab 3'
data1=soup.find_all(string='Galaxy Tab 3')
print(data1)

#to see for all 'Galaxy' device, we use regex
data2=soup.find_all(string=re.compile('Galaxy'))
print(data2)
