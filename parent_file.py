import requests
from bs4 import BeautifulSoup as bs
import urllib.request

url = 'file:///C:/Users/Swu1/GitHub%20Code/Python003-003/maoyan.html'
html = urllib.request.urlopen(url).read()
#print(html)
    
bs_data = bs(html, 'html.parser')
# print(bs_data)

alist = []
for tags in bs_data.find_all('div', attrs={'class': 'channel-detail movie-item-title'}, limit=10):
    for a_tags in tags.find_all('a'):
        alist.append(a_tags.get('href'))
# print(alist)

# for i in iter(alist):
#     urls_list = 'https://maoyan.com' + i
#     print(urls_list)
urls_list = ['https://maoyan.com' + i for i in iter(alist)]
print(urls_list)