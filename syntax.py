#!/usr/bin/python3
# -*- coding:UTF-8 -*-
"""
age = int(input("Age of the dog:"))
if age < 0 or age > 30:
    print("骗谁呢？")
elif age == 1:
    print("这狗子14了")
elif age == 2:
    print("这狗子22了")
else :
    suishu = 22 + (age - 2) * 5
    print("这狗子%d了"%(suishu))
"""
he = 0
i = 1
while i <= 100:
    he += i
    i += 1
print(he)
he = 0
for i in range(1, 101):
    he += i
print(he)
