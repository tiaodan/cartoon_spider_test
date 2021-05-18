import re
import requests
from lxml import etree
import os


# 函数定义

# 创建文件夹
def mkdir(path):
    # 判断是否存在文件夹如果不存在则创建为文件夹
    # 如果路径不存在会创建这个路径

    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


# 超时处理
def get(url, header):
    i = 0
    while i < 3:
        try:
            result = requests.get(url, headers=header, timeout=5)
            return result
        except requests.exceptions.RequestException:
            print("TIME OUT " + str(i+1))
            i += 1


# 补零操作
def zero_fill(path):
    file_list = os.listdir(path)
    for file in file_list:
        if not file.endswith('.txt'):
            # 补0 10表示补0后名字共10位
            filename = file.zfill(10)
            os.rename(path + '/' + file, path + '/' + filename)


# 下载文件
def dld_erocool(erocool_urls, local_path, head_type, file_type):
    # 功能
    # 下载erocool链接中的图片

    # erocool_urls
    # erocool链接

    # local_path
    # 下载位置，将在该位置创建文件夹

    # head_type
    # 1：长链接，下载一般尺寸；0：短连接，下载竖直方向特长尺寸（韩漫）
    for erocool_url in erocool_urls:
        print('------------------------------------')
        # 确定下载链接url中部，从erocool链接中提取
        url_mid = re.search('detail/(.*)o', erocool_url).group(1)

        # 确定下载链接url头部，由head_type确定
        if head_type == 1:
            url_head = 'https://search.pstatic.net/common?src=https://mi.404cdn.com/galleries/'
        elif head_type == 0:
            url_head = 'https://mi.404cdn.com/galleries/'

        # User Agent
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
            'Cookie': '_ga=GA1.2.99173477.1570796706; csrftoken=OK1ZGOurCtTNFgBhOEauJm3krQyQVR28xSP7Zu9EEv8MjiCgwdQyPyKqViaGkmG4; Hm_lvt_7fdef555dc32f7d31fadd14999021b7b=1570796701,1570941042; _gid=GA1.2.160071259.1570941044; Hm_lpvt_7fdef555dc32f7d31fadd14999021b7b=1570941059',
            'Connection': 'close'
        }

        # 请求
        print('\tURL:')
        print('\t\t' + erocool_url)
        response = get(erocool_url, header)
        # print(response.text)
        with open('temp.txt', 'wb') as file:
            file.write(response.content)

        # 选取数据：总页数、名称
        pic_num = int(
            re.search('(.*) 頁', etree.HTML(response.text).xpath('//div[@class = "ld_box"]/div/div/text()')[3]).group(1))
        ero_name = etree.HTML(response.text).xpath('//h1/text()')[0]
        ero_name = ero_name.replace('/', '-')
        ero_name = ero_name.replace(':', '-')

        # 创建文件夹
        local_ero_path = local_path + '/' + ero_name
        mkdir(local_ero_path)
        local_url_path = local_ero_path + '/url.txt'
        with open(local_url_path, 'w') as file:
            file.write(erocool_url)
        print('\t' + 'Local directory:')
        print('\t\t' + local_ero_path)

        for i in range(1, pic_num + 1):
            pic_name = str(i) + '.' + file_type
            pic_url = url_head + url_mid + '/' + pic_name
            local_name = local_ero_path + '/' + pic_name.zfill(10)

            # 判断是否存在文件
            exist = os.path.isfile(local_name)
            print('\t' + str(i) + '/' + str(pic_num))
            if not exist:
                print('\t\t' + 'State: no such file, to be downloaded')
                # 下载
                with open(local_name, 'wb') as file:
                    content_temp = get(pic_url, header)
                    file.write(content_temp.content)
                print('\t\t' + 'Download finished')

            else:
                # 判断文件是否有效
                if os.path.getsize(local_name) < 1024:
                    print('\t\t' + 'State: invalid file, to be downloaded')
                    # 下载
                    with open(local_name, 'wb') as file:
                        content_temp = get(pic_url, header)
                        file.write(content_temp.content)
                    print('\t\t' + 'Download finished')
                else:
                    print('\t\t' + 'State: downloaded already')

            size = str(round(os.path.getsize(local_name) / 1024, 2))
            print('\t\t' + 'File size: ' + size + ' KB')


# 主程序

# 下载位置，将在该位置创建文件夹
#local_path = "F:/temp/aira2temp/erocool"
local_path = "C:/A_software/B_jieya/cartoon"

# erocool链接
# https://zh.erocool.me/detail/1686650o321307.html
urls = [
    'https://en.erocool1.com/detail/1686650o321307.htm',
]

# 图片下载链接类型
# 1：长链接，下载一般尺寸；0：短连接，下载竖直方向特长尺寸（韩漫）
head_type = 1

# 图片类型
# 一般是jpg；小部分是png
file_type = 'jpg'

# 下载
dld_erocool(urls, local_path, head_type, file_type)