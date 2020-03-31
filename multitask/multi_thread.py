#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2020/3/27 17:17
# @Author: guohz-acmr
# @File  : multi_thread.py
import threading
import time
from queue import Queue


class HotPot(threading.Thread):
    def __init__(self, name):
        super(HotPot, self).__init__(name=name)

    def run(self):
        for i in range(5):
            print('thread--{}:{} persons hotpot and sing'.format(self.name, i))
            time.sleep(1)


"""
print('create threads')
for tnum in range(3):
    hotpot = HotPot('hotpot[{}]'.format(tnum))
    hotpot.start()
    # hotpot.join()
    time.sleep(1)
print('start all threads')
"""


class Kid(threading.Thread):
    def __init__(self, cond, name):
        super(Kid, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)
        self.cond.acquire()
        print('{}：妈妈, 我想吃烤山药'.format(self.name))
        self.cond.notify()
        self.cond.wait()
        time.sleep(1)
        print('{}：够咧，谢谢妈妈，妈妈真好！'.format(self.name))
        self.cond.notify()
        self.cond.release()
        i = 0
        while True:
            if i == 3:
                print('{}：妈妈，撑咧，明儿再吃吧'.format(self.name))
                event.set()
                break
            if not que.empty():
                print('{}吃了妈妈做的第{}个烤山药'.format(self.name, que.get()))
                i += 1
            else:
                print('{}：妈妈，山药烤好了吗？'.format(self.name))
            time.sleep(1)


class Mama(threading.Thread):
    def __init__(self, cond, name):
        super(Mama, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        self.cond.wait()
        time.sleep(1)
        print('{}：吃，吃大个滴，两个够不？'.format(self.name))
        self.cond.notify()
        self.cond.wait()
        print('{}：我这就给你做'.format(self.name))
        self.cond.release()
        time.sleep(2)
        for i in range(1, 9):
            if not event.isSet():
                print('{}放了第{}个烤山药在餐桌上'.format(self.name, i))
                que.put(i)
                time.sleep(3)
            else:
                event.clear()
                print('{}：嗯喃，明儿还做烤山药！'.format(self.name))
                break


event = threading.Event()
condition = threading.Condition()
que = Queue()
kid = Kid(condition, '墩墩')
mama = Mama(condition, '妈妈')
kid.start()
mama.start()
