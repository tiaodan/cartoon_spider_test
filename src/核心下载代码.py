# 批量下载图片,参数url-->下载链接（list） , savepath-->保存路径（list）
def batch_download_img(url, save_path):
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
        print('正在下载第', i+1, '张图片。。。。。。。。')
        with open(save_path[i], 'wb') as f:
            f.write(img_bin)
            f.close()
        print('第', i+1, '张图片下载完成！！！')

    print('无异常，批量下载图片完成！')
    batch_download_endtime = datetime.now()
    print('批量下载时间差==', (batch_download_endtime - batch_download_starttime).seconds, '秒')
    print('批量下载时间差==', (batch_download_endtime - batch_download_starttime).seconds/60, '分')
