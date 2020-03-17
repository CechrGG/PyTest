#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2020/3/16 17:32
# @Author: guohz-acmr
# @File  : function.py
"""func test module
    This is a func test module.
    go python go!!!
"""


def selfdef_sum(num1, num2):
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        return '参数类型错误，需为整数或小数'
    else:
        return num1 + num2


def division(num1, num2):
    if not (isinstance(num1, int) and isinstance(num2, int)):
        return '参数类型错误，需为整数'
    elif num2 == 0:
        return '被除数不能为0'
    else:
        remender = num1 % num2
        quotient = (num1 - remender) // num2
        return quotient, remender


def show_user(user_id, *name, sex='', **age):
    print('id:{}'.format(user_id) + ', name:{}'.format(name) +
          ', sex:{}'.format(sex) + ', age:{}'.format(age))



