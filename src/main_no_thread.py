from src.utils import util
from datetime import datetime

if __name__ == '__main__':
    chapter_url = 'https://www.mhz1.com/info/2.html'
    save_path_rootdir = 'C:/A_software/B_jieya/cartoon'  # 存储路径根目录
    # util.download_one_cartoon_all_chapter(chapter_url, save_path_rootdir)
    # util.download_one_cartoon_some_chapter(chapter_url, save_path_rootdir, 1, 2)

    process_startime = datetime.now()
    # 批量下载
    util.download_one_cartoon_some_chapter(chapter_url, save_path_rootdir, 76, 90)

    process_endtime = datetime.now()
    durn = (process_endtime - process_startime).seconds
    print('退出主线程, 任务结束时间=', durn, '秒')
    print('退出主线程, 任务结束时间=', durn/60, '分')


    # 测试下载10章哪个快？



