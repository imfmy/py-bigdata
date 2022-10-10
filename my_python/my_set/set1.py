# -*- coding:utf-8 -*-
a = [3, 1, 2, 1]
s1 = set(a)
s2 = {1, 3, 2}
print(s1, s2, type(s2))
# {1, 2, 3} {1, 2, 3} <class 'set'>
print(id(s1), id(s2), s1 == s2)
# 2992349591584 2992350778528 True
s01 = {}
s02 = set()
print(s01, s02)  # {} set()
print(type(s01), type(s02), bool(s02), s01 == s02)
# <class 'dict'> <class 'set'> False False
