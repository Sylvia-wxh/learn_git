import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from time import sleep

#伪装头部，random user agent + cookie
user_agent = UserAgent().chrome
cookie = '__mta=146119307.1597673420335.1597936594203.1597936642218.11; uuid_n_v=v1; uuid=60E1DA50E09311EA900DBD34D8258965B45ACDC2010B4B989557BD406D5D157F; mojo-uuid=aa9712850706c7e51a8894479bdf751a; _lxsdk_cuid=173fcc1b5d0c8-05591201a0b616-b7a1334-100200-173fcc1b5d0c8; _lxsdk=60E1DA50E09311EA900DBD34D8258965B45ACDC2010B4B989557BD406D5D157F; _csrf=ffd2b0f4f7176c4788b99810b3b5066039ec8522edd9e88b652305a37c33cec7; mojo-session-id={"id":"6fcfbd3bf79462d361bb1ef2872fab52","time":1597935738498}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597754709,1597847150,1597912637,1597935739; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597936698; __mta=146119307.1597673420335.1597936642218.1597936697980.12; mojo-trace-id=26; _lxsdk_s=1740c645f01-42a-862-7e5%7C%7C39'

header = {'user-agent': user_agent, 'cookie': cookie}

#读取处理猫眼主页面
maoyan = 'https://movie.douban.com/subject/1292052/'
response = requests.get(maoyan, headers = header)
bs_data = bs(response.text, 'html.parser')
print(bs_data)


# import requests
# from bs4 import BeautifulSoup as bs
# import urllib.request
# import lxml.etree

# url = 'file:///C:/Users/Swu1/GitHub%20Code/Python003-003/New.xml'

# html = urllib.request.urlopen(url).read()
# # print(html)
    
# selector = lxml.etree.XML(html)
# dd = selector.xpath('/bookstore/book[2]')
# print(len(dd))

# uuid_n_v=v1; uuid=F3FAF3A0E21211EA92FADB0AB124FC3B39ECCA7D245A42DC893EA8AA3711861E; mojo-uuid=32663ae8c72634f209b088af2ad9356e; _lxsdk_cuid=17406937de2ac-044e906fe77a818-4c302273-100200-17406937de3c8; _lxsdk=F3FAF3A0E21211EA92FADB0AB124FC3B39ECCA7D245A42DC893EA8AA3711861E; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597838163,1597936490; __mta=210591402.1597838163639.1597838635674.1597838639941.3; _csrf=314ac9e7863a094f0e72c037c830d3c575e6dac8e6a0c81a0b8ca1d531ed1ad8; mojo-trace-id=1; mojo-session-id={"id":"27f7a11de0bda4a0cc7523f67d9491bf","time":1597936490049}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597936490; _lxsdk_s=1740c6fd757-2d4-5f4-3aa%7C%7CNaN

# Cookie: __mta=146119307.1597673420335.1597936594203.1597936642218.11; uuid_n_v=v1; uuid=60E1DA50E09311EA900DBD34D8258965B45ACDC2010B4B989557BD406D5D157F; mojo-uuid=aa9712850706c7e51a8894479bdf751a; _lxsdk_cuid=173fcc1b5d0c8-05591201a0b616-b7a1334-100200-173fcc1b5d0c8; _lxsdk=60E1DA50E09311EA900DBD34D8258965B45ACDC2010B4B989557BD406D5D157F; _csrf=ffd2b0f4f7176c4788b99810b3b5066039ec8522edd9e88b652305a37c33cec7; mojo-session-id={"id":"6fcfbd3bf79462d361bb1ef2872fab52","time":1597935738498}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597754709,1597847150,1597912637,1597935739; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597936698; __mta=146119307.1597673420335.1597936642218.1597936697980.12; mojo-trace-id=26; _lxsdk_s=1740c645f01-42a-862-7e5%7C%7C39