#!/usr/bin/python3
# -*- coding: UTF-8 -*-
print("guoguo")
a, b, c, d, e, f = 1, 1.1, True, 1 + 1j, "a\
    aa", None
print(type(a), type(b), type(c), type(d), type(e), type(f))
a, b = 0, 1
while b < 100:
    print(b, end=",")
    a, b = b, a + b
string = "babyTellMeWhy"
print("\n" + string[:], end=" ")

print(0.33 + 0.1)
print(0.33 + 0.11)
