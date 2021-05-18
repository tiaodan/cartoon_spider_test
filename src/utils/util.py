'''
功能： 工具类

'''

import os
import requests
import re
import threading
from datetime import datetime
from lxml import html

# 定义变量
etree = html.etree  # xpath对象

# save_path_rootdir = 'C:/A_software/B_jieya/cartoon'  # 存储路径根目录
# save_path_cartoon_name = '/健身教练'  # 存储路径-漫画名
# save_path_cartoon_number = '/1/'  # 存储路径-漫画第 x 话
cartoon_website_root_url = 'https://mhz1.com'


# 线程类
class MyThread (threading.Thread):
    def __init__(self, thread_id, name, chapter_url, save_path_rootdir, start_chapter, end_chapter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        # self.counter = counter
        self.chapter_url = chapter_url
        self.save_path_rootdir = save_path_rootdir
        self.start_chapter = start_chapter
        self.end_chapter = end_chapter

    def run(self):
        print("开始线程：", '线程id=%3s' % self.thread_id, '名称=《%s》' % self.name, '存储根目录=%s' % self.save_path_rootdir,
              '开始章节=%3s' % self.start_chapter, '结束章节=%3s' %self.end_chapter)
        download_one_cartoon_some_chapter(self.chapter_url, self.save_path_rootdir, self.start_chapter, self.end_chapter)
        # print_time(self.name, self.counter, 5)
        print("结束线程：", '线程id=%3s' % self.thread_id, '名称=《%s》' % self.name)


# 创建文件夹
def mkdir(path):
    # 判断是否存在文件夹如果不存在则创建为文件夹
    # 如果路径不存在会创建这个路径

    folder = os.path.exists(path)
    if not folder:
        print('不是文件，创建中。。。。')
        os.makedirs(path)


# 创建文件
def mkfile(path):
    print('创建文件。。。')
    f = open(path, 'w')
    f.close()


# 下载图片
def download_img(imgurl, savepath):
    imgurl = "https://img.mhz1.com/attachment/comic/2020/06/10/202006102217571627.jpg"
    response = requests.get(imgurl)
    img_bin = response.content

    savepath = "C:/A_software/B_jieya/cartoon/1.jpg"
    with open(savepath, 'wb') as f:
        f.write(img_bin)
        f.close()
        print('写入成功！')


# 批量下载图片,参数url-->下载链接（list） , savepath-->保存路径（list）
# 参数：cartoon_name 名称
# 参数：cartoon_chapter 章节
def batch_download_img(cartoon_name, cartoon_chapter, url, save_path):
    '''
    imgurls = list()
    imgurls_base = 'https://img.mhz1.com/attachment/comic/2020/06/10/'
    imgurls_name = ['202006102217571627.jpg', '202006102219186974.jpg', '202006102219229415.jpg', '202006102219257367.jpg',
                    '202006102220244157.jpg', '202006102220347185.jpg', '202006102220357309.jpg', '202006102220438882.jpg',
                    '202006102220484213.jpg', '202006102220506768.jpg', '202006102220561278.jpg', '202006102221007690.jpg',
                    '202006102221035790.jpg', '202006102221128107.jpg']
    for i in range(len(imgurls_name)):
        # imgurls.append(imgurls_base + imgurls_name[i])
        imgurls.append(imgurls_base + imgurls_name[i])
    '''
    print('批量下载链接列表长度==', len(url))
    print('批量下载链接列表==', url)

    batch_download_starttime = datetime.now()
    # 请求数据 并下载
    for i in range(len(url)):
        # 请求
        response = requests.get(url[i])
        img_bin = response.content
        # savepath = "C:/A_software/B_jieya/cartoon/" + str(i+1) + '.jpg'

        # 下载
        print('漫画名=%s' % cartoon_name, '第%s章' %cartoon_chapter, ', 第%s张图片正在下载.................' % (i+1))
        with open(save_path[i], 'wb') as f:
            f.write(img_bin)
            f.close()
        print('漫画名=%s' % cartoon_name, '第%s章' %cartoon_chapter, ', 第%s张图片下载完成！！！' % (i+1))

    print('无异常，批量下载图片完成！')
    batch_download_endtime = datetime.now()
    print('批量下载时间差==', (batch_download_endtime - batch_download_starttime).seconds, '秒')
    print('批量下载时间差==', (batch_download_endtime - batch_download_starttime).seconds/60, '分')


# 时间相关-暂时未用-用来参考
def gettime():
    from datetime import datetime
    import time

    a = datetime.now()  # 获得当前时间
    time.sleep(2)  # 睡眠两秒
    b = datetime.now()  # 获取当前时间
    durn = (b - a).seconds  # 两个时间差，并以秒显示出来   # type -->int
    print(durn)

    timeshow = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间 ，并以当前格式显示
    print(timeshow)
    """
    打印：
    2
    2019 - 06 - 03
    """


# xpath定位代码-没用，打开文件
def xpath_html():
    pass
    """
    from lxml import etree
    etree = html.etree
    f = open("../configure/a.html", "r", encoding="utf-8")  # 读取文件
    f = f.read()　　  # 把文件内容转化为字符串
    html = etree.HTML(f)  # 把字符串转化为可处理的格式-->xpath定位出来的是一个对象    """


# xpath定位html-没用
def get_html_imgs_nouse():
    # etree = html.etree
    tree = etree.parse('test.html')
    # print(tree.xpath('//div[@class="rd-article-wr clearfix"]'))
    r1 = tree.xpath('/html/body/div')  # 直接从上往下挨着找节点
    r2 = tree.xpath('/html//div')  # 跳跃了一个节点来找到这个div节点的对象
    r3 = tree.xpath('//div')  ##跳跃上面所有节点来寻找div节点的对象
    r4 = tree.xpath('//div[@class="song"]/p[3]')  # 这个索引是从1开始的
    r5 = tree.xpath('//div[@class="tang"]//li[5]/a/text()')  # 定位杜牧文本, type = list
    r6 = tree.xpath('//div[@class="song"]/img/@src')  # 直接输出就是文本，定位属性
    r7 = tree.xpath('//@href')
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(type(r5))
    print(r6)
    print(r7, '\n')


'''
#  获取图片下载链接和保存名称，返回dict ,参数:html_context(str)
# save_path_rootdir = 'C:/A_software/B_jieya/cartoon'  # 存储路径根目录
# save_path_cartoon_name = '/健身教练'  # 存储路径-漫画名
# save_path_cartoon_number = '/1/'  # 存储路径-漫画第 x 话
'''


def get_html_imgs(html_context, save_path_rootdir, save_path_cartoon_name, save_path_cartoon_number):
    # parser = etree.HTMLParser(encoding="utf-8")  # 解析本地html文件用到-->因为怕不是严格的xml文件
    # tree = etree.parse(html_context, parser=parser)  # 解析本地html文件用到
    # tree = etree.HTML(html_context, parser=parser)  # 解析网络请求回来的html 用到
    tree = etree.HTML(html_context)  # 加不加parser都可以

    # 获取图片下载链接
    img_links_list = tree.xpath('//div[@class="rd-article-wr clearfix"]/div/img/@data-original')
    for i in range(len(img_links_list)):
        # print('=============================================', type(img_links_list[i]))
        print('根据属性获取图片下载链接，长度=', len(img_links_list), '当前第%3s' %(i+1), ', 链接=', img_links_list[i])

    # 获取图片保存名称，并重构成完整保存链接 --》 C:/根目录/漫画名/第几话/x.jpg
    img_save_names_list = tree.xpath('//div[@class="rd-article-wr clearfix"]/div/img/@alt')  # 图片另存为的名称list,只是显示1.jpg这些
    for i in range(len(img_save_names_list)):
        img_save_names_list[i] = save_path_rootdir + save_path_cartoon_name + save_path_cartoon_number \
                                 + img_save_names_list[i]
        print('保存的图片名称list，长度=', len(img_save_names_list), '当前第%3s' %(i+1), ', 图片名称=', img_save_names_list[i])

    # 返回字典
    img_dict = {'img_links': img_links_list, "img_save_names": img_save_names_list}
    return img_dict


# 通过网页地址，获取html,返回str html
def get_html(url):
    response = requests.get(url)
    # html_text = response.content  # 2进制类型
    html_context = response.text  # str类型
    return html_context

    # print(type(response))    # class类型
    # print(type(html_text), '\n')
    # print(type(html_context))


# 去除\r\t\n等特殊符号,参数list, 返回还是list
def remove_special_symbol():
    pass
    # 截取纯数字，把纯数字替换
    my_str = re.sub("\D", "", my_str)


# 字符串相关代码
def use_str_nouse():
    cartoon_numbers[i].strip()[1:-1]  # 去除\r\t\n等特殊换行符，并截取第1位-》倒数第2位（包括倒数第二位）

    # 截取纯数字，把纯数字替换
    my_str = re.sub("\D", "", my_str)


# 获取某一部漫画（比如：健身教练）的所有信息，没话对应的url,漫画名、等, 返回字典
def get_cartoon_info(url):
    # 获取网页 str
    html_context = get_html(url)

    # 解析每话对应url
    tree = etree.HTML(html_context)

    # 1. 获取漫画名称
    cartoon_name = tree.xpath('//p[@class="comic-title j-comic-title"]/text()')[0]  # 返回list,['健身教练']，所以截取index=0
    print('漫画名称==', cartoon_name, '， 类型==', type(cartoon_name))

    # 2. 获取第几话
    # cartoon_numbers = tree.xpath('normalize-space(//div[@class="chapter__list clearfix"]/ul/li/a/text())')  # 解决 带\n\t\r等内容->不好用
    cartoon_numbers = tree.xpath('//div[@class="chapter__list clearfix"]/ul/li/a/text()')  # 此方法结果带\n\t\r等内容
    # /去除多余特殊字符（第几话）
    for i in range(len(cartoon_numbers)):
        # print('list元素类型', type(cartoon_numbers[i]))   # <class 'lxml.etree._ElementUnicodeResult'>,能用.strip()方法
        cartoon_numbers[i] = re.sub('\D', '', cartoon_numbers[i])
    print('xpath所有章节=', cartoon_numbers)

    # 3. 获取章节下载链接
    cartoon_numbers_urls = tree.xpath('//div[@class="chapter__list clearfix"]/ul/li/a/@href')
    for i in range(len(cartoon_numbers_urls)):
        # 重构url，url= /chapter/72310.html -->加上完整网址
        cartoon_numbers_urls[i] = cartoon_website_root_url + cartoon_numbers_urls[i]

    """
    for i in range(len(cartoon_numbers)):
        print('排序前，漫画号码，长度=', len(cartoon_numbers), '当前index=%3s' % (i+1), '章节=%3s' % cartoon_numbers[i],
              '下载链接=', cartoon_numbers_urls[i])
    """
    # 4. 重新排序漫画第几章--》url.思路：先转成dict,排序后，再重新拆成list,(排序前把key转成int,之后还转成str,因为xpath默认就是str)
    cartoon_chapters_and_urls_dict = dict()
    for i in range(len(cartoon_numbers)):
        # 给dict添加数据{'章节':'下载链接'} key为什么用int，见test_sort_dict_key.py
        cartoon_chapters_and_urls_dict[int(cartoon_numbers[i])] = cartoon_numbers_urls[i]
    print('排序前dict==,长度=', len(cartoon_chapters_and_urls_dict), ', 类型=', type(cartoon_chapters_and_urls_dict),
          cartoon_chapters_and_urls_dict)
    cartoon_chapters_and_urls_list = sorted(cartoon_chapters_and_urls_dict.items(), key=lambda x: x[0])   # x: x[0]表示键
    print('排序后dict==,长度=', len(cartoon_chapters_and_urls_list), ', 类型=', type(cartoon_chapters_and_urls_list),
          cartoon_chapters_and_urls_list)

    # 5. 将重排序的 {‘章节’：‘下载链接’}，拆分成list
    for i in range(len(cartoon_chapters_and_urls_list)):
        cartoon_numbers[i] = str(cartoon_chapters_and_urls_list[i][0])
        cartoon_numbers_urls[i] = cartoon_chapters_and_urls_list[i][1]
    # 打印
    """
    for i in range(len(cartoon_numbers)):
        print('排序后，漫画号码，长度=', len(cartoon_numbers), '当前index=%3s' % (i + 1), '章节=%3s' % cartoon_numbers[i],
              '下载链接=', cartoon_numbers_urls[i])
    """

    # 6. 返回数据, cartoon_numbers：内容是int, cartoon_number_urls:内容是str
    cartoon_info = {'cartoon_name': cartoon_name, 'cartoon_numbers': cartoon_numbers, 'cartoon_number_urls': cartoon_numbers_urls}
    return cartoon_info


# 指定多少获取某一部漫画（比如：健身教练）的所有信息，没话对应的url,漫画名、等, 返回字典
def get_cartoon_info_by_number(url):
    # 获取网页 str
    html_context = get_html(url)

    # 解析每话对应url
    tree = etree.HTML(html_context)

    # 漫画名称
    cartoon_name = tree.xpath('//p[@class="comic-title j-comic-title"]/text()')[0]  # 返回list,['健身教练']，所以截取index=0
    print('漫画名称==', cartoon_name, '， 类型==', type(cartoon_name))

    # /第几话
    # cartoon_numbers = tree.xpath('normalize-space(//div[@class="chapter__list clearfix"]/ul/li/a/text())')  # 解决 带\n\t\r等内容->不好用
    cartoon_numbers = tree.xpath('//div[@class="chapter__list clearfix"]/ul/li/a/text()')  # 此方法结果带\n\t\r等内容
    # /去除多余特殊字符（第几话）
    for i in range(len(cartoon_numbers)):
        # print('list元素类型', type(cartoon_numbers[i]))   # <class 'lxml.etree._ElementUnicodeResult'>,能用.strip()方法
        cartoon_numbers[i] = re.sub('\D', '', cartoon_numbers[i])
    print(cartoon_numbers)
    for i in range(len(cartoon_numbers)):
        print('漫画号码，长度=', len(cartoon_numbers), '当前第%3s' %(i+1), ', 对应号码=', cartoon_numbers[i])

    # /请求url
    cartoon_numbers_urls = tree.xpath('//div[@class="chapter__list clearfix"]/ul/li/a/@href')
    for i in range(len(cartoon_numbers_urls)):
        # 重构url，url= /chapter/72310.html -->加上完整网址
        cartoon_numbers_urls[i] = cartoon_website_root_url + cartoon_numbers_urls[i]
        print('漫画号码对应url，长度=', len(cartoon_numbers_urls), '当前第%3s' %(i+1), ', 对应url=', cartoon_numbers_urls[i])

    # 返回数据
    cartoon_info = {'cartoon_name': cartoon_name, 'cartoon_numbers': cartoon_numbers, 'cartoon_number_urls': cartoon_numbers_urls}
    return cartoon_info


# 下载某部漫画所有章节图片
# 参数：1.chapter_url：章节下载链接  2.save_path_rootdir：存储路径根目录
def download_one_cartoon_all_chapter(chapter_url, save_path_rootdir):
    # 获取某一部漫画的信息，多少章，每一章的下载链接
    # cartoon_info = util.get_cartoon_info('https://www.mhz1.com/info/2.html')
    cartoon_info = get_cartoon_info(chapter_url)

    # '''
    # 下载某部漫画所有照片
    if cartoon_info is not None:
        # 定义变量
        cartoon_name = cartoon_info['cartoon_name']  # 漫画名称list
        cartoon_numbers = cartoon_info['cartoon_numbers']  # 漫画集数list
        cartoon_number_urls = cartoon_info['cartoon_number_urls']  # 漫画每集url(list)

        # save_path_rootdir = 'C:/A_software/B_jieya/cartoon'  # 存储路径根目录
        # save_path_cartoon_name = '/健身教练1'  # 存储路径-漫画名
        save_path_cartoon_name = '/' + cartoon_name  # 存储路径-漫画名
        print('漫画名称type===========================', type(save_path_cartoon_name))

        for i in range(len(cartoon_numbers)):
            # save_path_cartoon_number = '/1/'  # 存储路径-漫画第 x 话
            save_path_cartoon_number = '/' + cartoon_numbers[i] + '/'  # 存储路径-漫画第 x 话

            # 请求网页获取网页html
            # html_context = util.get_html('https://www.mhz1.com/chapter/4.html')
            html_context = get_html(cartoon_number_urls[i])

            # 解析html 获取图片下载链接和 保存名称
            img_dict = get_html_imgs(html_context, save_path_rootdir, save_path_cartoon_name,
                                          save_path_cartoon_number)

            # 创建目录
            mkdir(save_path_rootdir + save_path_cartoon_name + save_path_cartoon_number)

            print('图片下载链接', img_dict['img_save_names'])

            # 批量下载,自动创建文件
            batch_download_img(cartoon_name, cartoon_numbers[i], carimg_dict['img_links'], img_dict['img_save_names'])
    # '''


# 下载某部漫画部分章节
# 参数：1.chapter_url：章节下载链接  2.save_path_rootdir：存储路径根目录
# 参数：3.start_chapter：开始章节(int)  2.end_chapter：终止章节(int)
def download_one_cartoon_some_chapter(chapter_url, save_path_rootdir, start_chapter, end_chapter):
    # 获取某一部漫画的信息，多少章，每一章的下载链接
    # cartoon_info = util.get_cartoon_info('https://www.mhz1.com/info/2.html')
    cartoon_info = get_cartoon_info(chapter_url)

    # '''
    # 下载某部漫画所有照片
    if cartoon_info is not None:
        # 定义变量
        cartoon_name = cartoon_info['cartoon_name']  # 漫画名称list
        cartoon_numbers = cartoon_info['cartoon_numbers']  # 漫画集数list
        cartoon_number_urls = cartoon_info['cartoon_number_urls']  # 漫画每集url(list)

        # save_path_rootdir = 'C:/A_software/B_jieya/cartoon'  # 存储路径根目录
        # save_path_cartoon_name = '/健身教练1'  # 存储路径-漫画名
        save_path_cartoon_name = '/' + cartoon_name  # 存储路径-漫画名
        print('漫画名称type===========================', type(save_path_cartoon_name))

        print('传的参数类型=', type(start_chapter))  # 传的还是int
        some_cartoon_numbers = cartoon_numbers[start_chapter - 1: end_chapter]  # 截取某几章
        some_cartoon_number_urls = cartoon_number_urls[start_chapter - 1: end_chapter]  # 截取某几章对应的urls
        for i in range(len(some_cartoon_numbers)):
            # save_path_cartoon_number = '/1/'  # 存储路径-漫画第 x 话
            print('*'*50, '下载第N话==', some_cartoon_numbers[i])
            print('*'*50, '下载第N话,urls==', some_cartoon_number_urls[i])
            save_path_cartoon_number = '/' + some_cartoon_numbers[i] + '/'  # 存储路径-漫画第 x 话

            # 请求网页获取网页html
            # html_context = util.get_html('https://www.mhz1.com/chapter/4.html')
            html_context = get_html(some_cartoon_number_urls[i])

            # 解析html 获取图片下载链接和 保存名称
            img_dict = get_html_imgs(html_context, save_path_rootdir, save_path_cartoon_name,
                                     save_path_cartoon_number)

            # 创建目录
            mkdir(save_path_rootdir + save_path_cartoon_name + save_path_cartoon_number)

            print('图片下载链接', img_dict['img_save_names'])

            # 批量下载,自动创建文件
            batch_download_img(cartoon_name, some_cartoon_numbers[i], img_dict['img_links'], img_dict['img_save_names'])
    # '''


# 线程管理
# 返回list, 线程对象
# 参数：thread_id： 线程id (int)
# 参数：thread_name : 线程名称 (str)
# 参数：chapter_url ： 章节请求url (str)
# 参数：save_path_rootdir : 保存路径根目录 (str)
# 参数：start_chapter ： 开始章节号(int)
# 参数：end_chapter ： 结束章节号(int)
def thread_manage(thread_id, thread_name, chapter_url, save_path_rootdir, start_chapter, end_chapter):
    # thread_obj_list = util.MyThread(1, '线程1', chapter_url, save_path_rootdir, start_chapter, end_chapter)
    thread_pool = list()  # 线程池

    # 创建线程
    for i in range(end_chapter - start_chapter + 1):
        # print(' dangqina zhangjie===', start_chapter)
        thread = MyThread(thread_id, thread_name + str(thread_id), chapter_url, save_path_rootdir, start_chapter, end_chapter)
        thread_pool.append(thread)  # 加入线程池
        thread_id += 1
        start_chapter += 1

    # 启动线程
    for i in range(len(thread_pool)):
        thread_pool[i].start()
    # 等待所有线程终止，才进入主进程
    for i in range(len(thread_pool)):
        thread_pool[i].join()
    return thread_pool  # 返回线程池list,里面包含线程对象
