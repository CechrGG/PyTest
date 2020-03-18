#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time  : 2020/3/18 14:14
# @Author: guohz-acmr
# @File  : bases.py


class User(object):
    def __init__(self, uid, name, email):
        self.uid = uid
        self.name = name
        self.email = email

    def to_string(self):
        print('id:{}, name:{}, email:{}'.format(self.uid, self.name, self.email))

    def user(self):
        print('It\'s User : ' + self.name)


wo = User(1, 'guoguo', '@email.com')
User.to_string(wo)
User.user(wo)
user = User(2, 'qianqian', '')
user.to_string()
user.user()
