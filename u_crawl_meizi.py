import requests
from bs4 import BeautifulSoup
import os

headers = {'user-agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}   
all_url='http://www.mzitu.com/all'  #the beginning of urls
start_html=requests.get(all_url,headers=headers) #use the method 'get()' to get all_url's content
Soup=BeautifulSoup(start_html.text,'lxml')
all_a=Soup.find('div',class_='all').find_all('a')
for a in all_a:
    title=a.get_text() 
    href=a['href'] 
    #continue crawl
    html=requests.get(href,headers=headers)
    html_Soup=BeautifulSoup(html.text,'lxml')
    max_span=html_Soup.find('div',class_='pagenavi').find_all('span')[-2].get_text() #a page content

    for page in range(1,int(max_span)+1):
        page_url=href+'/'+str(page)
        print(page_url)   #the url of picture

