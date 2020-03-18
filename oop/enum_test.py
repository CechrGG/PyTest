#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2020/3/18 17:03
# @Author: guohz-acmr
# @File  : enum_test.py
from enum import Enum, unique

week = Enum('Week', ('Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'))
for day, member in week.__members__.items():
    print('{}---{}---{}---{}'.format(week.Wed, day, member.name, member.value))


@unique
class MyWeek(Enum):
    Mon = '星期一'
    Tues = '星期二'
    Wed = '星期三'
    Thur = '星期四'
    Fri = '星期五'
    Sat = '星期六'
    Sun = '星期日'


for name, member in MyWeek.__members__.items():
    print('{}---{}'.format(name, member.value))
print(MyWeek.Fri.value)
