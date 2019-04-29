#!/usr/bin/python3
# -*- coding:UTF-8 -*-
import math

def myAbs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0 :
        return x
    else :
        return -x
#print(myAbs("a"))

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(math.radians(angle))
    ny = y + step * math.sin(math.radians(angle))
    return nx, ny
nx, ny = move(1,1,5,30)
print("%.2f %.2f" % (nx, ny))

def quadratic(a, b, c):
    for arg in (a, b, c):
        if not isinstance(arg, (int, float)):
            raise TypeError("bad args")
    if a == 0:
        x1 = - c/b
        return x1
    else:
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        return x1, x2

ret = quadratic(1, 4, 4)
print(ret)

def test_func(a, b, *args, c=0, **kw):
    print(a, b, args, c, kw)
arg = [3, 4]
test_func(1, 2, *arg, other="other")

def product(*args):
    if len(args) <= 0:
        raise TypeError("none")
    else:
        ret = 1
        for arg in args:
            ret *= arg
        return ret
print(product(5,6))

def fact(n):
    if n == 1:
        return n
    else :
        return n*fact(n -1)
print(fact(10))

def fact_opti(n):
    return fact_iter(n, 1)
def fact_iter(n, ret):
    if n == 1:
        return ret
    else:
        return fact_iter(n-1, ret*n)
print(fact_opti(1000))
# 遗憾的是python解释器并没有做优化，依然溢出