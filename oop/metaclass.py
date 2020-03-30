#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2020/3/27 16:57
# @Author: guohz-acmr
# @File  : metaclass.py


class Meta(object):
    pass


mc = type("Meta", (), {})
meta = Meta()
print(type(mc))
print(type(meta))
