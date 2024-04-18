import requests
from bs4 import BeautifulSoup

url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
r=requests.get(url)

#BeautifulSoup deals with Xml data

soup=BeautifulSoup(r.text, 'lxml')

#for price of the tablets mentioned in sites

prices=soup.findAll('h4', class_='price float-end card-title pull-right')
# print(prices)

