import requests
from bs4 import BeautifulSoup as bs
import urllib.request
import lxml.etree
from time import sleep
import pandas

url = 'file:///C:/Users/Swu1/GitHub%20Code/Python003-003/details.html'
html = urllib.request.urlopen(url).read().decode('utf-8')
#print(html)

selector = lxml.etree.HTML(html)

film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
# print(f'电影名字：{film_name}')

film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[@*]/text()')
# print(f'电影类型：{film_type}')

film_time = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
# print(f'上映时间：{film_time}')
file1 = [film_name film_type film_time]
# print(file1)

test = pandas.DataFrame(data = file1)
test.to_csv('./test.csv', encoding='gbk', index=False, header=False)

# def child_content (myUrl):
#     html = urllib.request.urlopen(myUrl).read().decode('utf-8')

#     selector = lxml.etree.HTML(html)
	
# 	film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
#     # print(f'电影名字：{film_name}')

#     film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a[@*]/text()')
#     # print(f'电影类型：{film_type}')

#     film_time = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
#     # print(f'上映时间：{film_time}')
	
#     return ([film_name, film_type, film_time])

# urls_list = ['file:///C:/Users/Swu1/GitHub%20Code/Python003-003/details.html', 'file:///C:/Users/Swu1/GitHub%20Code/Python003-003/babai.html']

# film_list = []
# for page in urls_list:
#     film_list.append(child_content(page))
#     sleep(5)
# print(film_list)
