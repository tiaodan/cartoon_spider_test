# *_* coding:UTF-8 *_*
# 开发人员：12861
# 开发时间： 0:13
# 文件名称：test2.PY
# 开发工具：PyCharm

import requests
from lxml import html

tree = html.etree

response = requests.get('https://www.mhz1.com/info/2.html')
cartoon_name = tree.xpath('//p[@class="comic-title j-comic-title"]/text()')
