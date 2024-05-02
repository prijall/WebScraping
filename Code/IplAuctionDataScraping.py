import requests 
import pandas as pd
from bs4 import BeautifulSoup


url='https://www.iplt20.com/auction'
r= requests.get(url)

#print(r)  #for checking response status


soup=BeautifulSoup(r.text, 'lxml')
tables=soup.find('table', class_="ih-td-tab auction-tbl")
#print(tables)
header=tables.find_all('th')
titles=[]


for i in header:
    title=i.text
    titles.append(title)

#print(titles)


df=pd.DataFrame(columns=titles)
#print(df)

rows=tables.find_all('tr')
print(rows)

for i in rows[1:]:
    first_td=i.find_all('td')[0].find('div', class_='ih-pt-ic').text.strip()
    data=i.find_all('td')[1:]
    row=[tr.text for tr in data]
    row.insert(0, first_td)
    l=len(df)
    df.loc[l]=row

# print(df)


df.to_csv('IPL Auction 2024_01.csv')