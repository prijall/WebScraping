import requests

url='https://webscraper.io/test-sites/e-commerce/allinone'
r=requests.get(url)
#print(r.status_code) #to check https response status wherther the site allows to us 
                    #scraper or not

print(r.text)   #for whole html of the site
