#!/usr/bin/python3

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 10)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        # print ("%s: %s" % (threadName, time.ctime(time.time())))
        print (threadName)
        counter -= 1


# 创建新线程
# thread1 = myThread(1, "1111111111111", 1)
# thread2 = myThread(2, "2222222222222", 1)
thread1 = myThread(1, "1111111111111", 1)
thread2 = myThread(1, "2222222222222", 1)
thread3 = myThread(1, "3333", 1)  # id相同没事

# 开启新线程
thread1.start()
thread2.start()
thread3.start()
thread1.join()
# thread2.join()
print("退出主线程")