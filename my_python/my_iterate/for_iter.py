l: list[int] = [1, 2, 3]
for i in l:
    print(i)
    # 1
    # 2
    # 3
for i in iter(l):
    print(i)
    # 1
    # 2
    # 3
l1: list[int] = [7, 8, 9]
iterator = iter(l1)
print(iterator, type(iterator))
# <list_iterator object at 0x000002D46E3C3FD0> <class 'list_iterator'>
t1 = tuple(iterator)
print(t1, type(t1))
# (7, 8, 9) <class 'tuple'>
l2: list[int] = list(iterator)
print(l2, type(l2))
# [] <class 'list'> ##迭代器只能用一次?
# //a,b,c:int = t1 ## 变量注解不能与元组解包组合
# //print(max(iterator))  ## ValueError: max() arg is an empty sequence
print(max(t1), max(iter(l)))
# 9 3
