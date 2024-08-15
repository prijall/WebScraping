import requests
from bs4 import BeautifulSoup

url='https://www.flipkart.com/search?q=phone+under+20000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_11_na_na_na&as-pos=2&as-type=RECENT&suggestionId=phone+under+20000%7CMobiles&requestId=7eb684fe-b566-4b28-bc1d-0b126f1d7aeb&as-searchtext=phone%20under%2020000'
r=requests.get(url)
#print(r)

soup=BeautifulSoup(r.text, 'lxml')
# print(soup)

while True:
    nextpage=soup.find('a', class_='_9QVEpD').get('href')
    #print(nextpage)
    cnp="https://www.flipkart.com/" + nextpage
    print(cnp)

    url=cnp
    r=requests.get(url)
    soup=BeautifulSoup(r.text, 'lxml')