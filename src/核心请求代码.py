# *_* coding:UTF-8 *_*
# 开发人员：12861
# 开发时间： 0:15
# 文件名称：核心请求代码.PY
# 开发工具：PyCharm

import requests
from lxml import html

# 1. 创建etree，相当于DOM
etree = html.etree

# 2. 请求url
response = requests.get('https://www.mhz1.com/info/2.html')
html_text = response.text  # str类型的html

# 3. 有些html格式不规范，少/闭环，解析成完整html
tree = etree.HTML(html_text)

# 4. xpath定位
cartoon_name = tree.xpath('//p[@class="comic-title j-comic-title"]/text()')
# cartoon_name = tree.xpath('//div[@class="de-info__box"]/p[@class="comic-title j-comic-title"]/text()')

# 5. 打印
print(type(cartoon_name))
print(cartoon_name[0])
print(cartoon_name)
print(type(cartoon_name[0]))  # <class 'lxml.etree._ElementUnicodeResult'>,可以直接当str用
print(type(str(cartoon_name[0])))

