import requests
from bs4 import BeautifulSoup as bs
import urllib.request
import lxml.etree

# 本地版
url = 'file:///C:/Users/Swu1/GitHub%20Code/Python003-003/maoyan.html'
html = urllib.request.urlopen(url).read().decode('utf-8')
# print(html)
    
selector = lxml.etree.HTML(html)
dd = selector.xpath('/html/body/div[4]/div/div[2]/div[2]/dl/dd/div[2]')
print(dd)

# print(selector.xpath('/html/body/div[4]/div/div[2]/div[2]/dl/dd'))

# alist = []
# for tag in range(1, 10):
#     num = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[tag]/div[2]/a/@href')
#     print(num)
    # alist.append(num)
# print(alist)

# urls_list = ['https://maoyan.com' + i for i in iter(alist)]
# print(urls_list)

# 网页版
# from fake_useragent import UserAgent
# myUrl = 'https://maoyan.com/films?showType=3'

# ua = UserAgent()
# header = {}
# header['user-agent'] = ua.chrome

# response = requests.get(myUrl, headers = header)
# selector = lxml.etree.HTML(response.text)

# alist = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[10]/div[2]/a/@href')
# print(alist)