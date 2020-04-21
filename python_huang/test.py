# -*- coding: UTF-8 -*-
"""

Author: 笑笑
Date: 20200315
"""

import requests
from bs4 import BeautifulSoup

# url = 'https://news.qq.com'
url = 'https://zmister.com'
data = requests.get(url).text

soup = BeautifulSoup(data,'lxml')

new_title = soup.select('a')

for n in new_title:

    title = n.get_text()
    link = n.get('href')
    if title != '' and link !='' :
        data = {
            '标题':title,
            '链接':link
        }
        print(data)

