import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent


myUrl = 'https://maoyan.com/films?showType=3'

ua = UserAgent()

header = {}
header['user-agent'] = ua.chrome

response = requests.get(myUrl, headers = header)
# # print(f'返回码是：{pageContent.status_code}')
# # print(pageContent.text)

bs_data = bs(response.text, 'html.parser')
# print(bs_data.text)

# for tags in bs_data.find_all('div', attrs={'class': 'channel-detail movie-item-title'}, limit=10):
#     for atags in tags.find_all('a',):
#         print(atags.get('href'))

#取child page后缀，形成链接
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