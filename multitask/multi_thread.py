#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2020/3/27 17:17
# @Author: guohz-acmr
# @File  : multi_thread.py
import threading
import time


class HotPot(threading.Thread):
    def __init__(self, name):
        super(HotPot, self).__init__(name=name)

    def run(self):
        for i in range(5):
            print('thread--{}:{} persons hotpot and sing'.format(self.name, i))
            time.sleep(1)


print('create threads')
for tnum in range(3):
    hotpot = HotPot('hotpot[{}]'.format(tnum))
    hotpot.start()
    hotpot.join()
    time.sleep(1)
print('start all threads')
