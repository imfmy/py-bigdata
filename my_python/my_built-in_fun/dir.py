# -*- coding: utf-8 -*-
# def dir(__o: object = ...) -> list[str]
print(dir())  # 获取当前模块的方法
# ['__annotations__', '__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__', '__spec__']
print(dir([]))  # 获取对象-列表的信息
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
# '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
# '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count',
# 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
a = 1
print(dir(a))  # 获取整数对象的信息
print(dir("a"))  # 获取字符串对象的信息


class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']

