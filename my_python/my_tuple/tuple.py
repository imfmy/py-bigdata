"""元组是Python内置(builtins)不可变(immutable)的可迭代(iterable)序列"""
# -*- coding:utf-8 -*-
lt1 = [1, 2, 3]
lt2 = list(lt1)
lt3 = [1, 2, 3]
print(type(lt1), lt1 == lt2 == lt3)  # <class 'list'> True
print(id(lt1), id(lt2), id(lt3))  # 1978092507776 1978092510528 1978092345536

tp1 = 1,
tp2 = tuple(tp1)
tp3 = (1,)
print(type(tp1), tp1 == tp2 == tp3)  # <class 'tuple'> True
print(tp1, bool(tp1))  # (1,) True
print(id(tp1), id(tp2), id(tp3))  # 2377582226256 2377582226256 2377582226256

# 创建空元组
tp01 = ()
tp02 = tuple()
print(type(tp01), type(tp02))
# <class 'tuple'> <class 'tuple'>
print(tp01, tp02, bool(tp01), tp02 == tp01)
# () () False True
tp1 = (1, 2, 3)
tp2 = (1, 2, 3,)
print(tp1 == tp2, id(tp1), id(tp2))  # True 1738638607488 1738638607488
print(len(tp1))  # 3

# 当拆分元组时，对于元组中不需要的信息，可以用“_”表示，不用再额外定义变量名
user_info = ("Jack", "12", "135xxxxxxx", "boy")
print(user_info, type(user_info))
name, _, _, gender = user_info
print(f'name={name}, gender={gender}')
# name=Jack, gender=boy
print(_)
# 135xxxxxxx