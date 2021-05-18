# from src.utils import util
from utils import util
from datetime import datetime

if __name__ == '__main__':
    # 定义变量
    chapter_url = 'https://www.mhz1.com/info/2.html'
    save_path_rootdir = 'C:/A_software/B_jieya/cartoon'  # 存储路径根目录
    start_chapter = 79  # 开始章节
    end_chapter = 80  # 结束章节
    thread_id = start_chapter  # 线程id
    thread_name = '线程-下载章节'
    process_startime = datetime.now()  # 计算时间

    # 开启线程
    # thread1 = util.MyThread(79, '线程1', chapter_url, save_path_rootdir, 79, 79)
    # thread2 = util.MyThread(80, '线程1', chapter_url, save_path_rootdir, 80, 80)
    # thread1.start()
    # thread2.start()
    # thread1.join()
    # thread2.join()
    thread_pool = util.thread_manage(thread_id, thread_name, chapter_url, save_path_rootdir, start_chapter, end_chapter)
    # print('线程池=====', thread_pool)

    # 计算时间
    process_endtime = datetime.now()
    durn = (process_endtime - process_startime).seconds
    print('退出主进程, 任务结束时间=', durn, '秒')
    print('退出主进程, 任务结束时间=', durn/60, '分')




