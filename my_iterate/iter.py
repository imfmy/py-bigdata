# l = [1, 2, 3]
# l = (1,2,3)
# l = {1: 10, 2: 20, 3: 30}
l: str = '123'
# //l=1  # TypeError: 'int' object is not iterable
it1 = iter(l)
print(it1, type(it1))
# <list_iterator object at 0x000001B60161C5B0> <class 'list_iterator'>
print(it1.__next__())  # 1
print(it1.__next__())  # 2
print(it1.__next__())  # 3
# //print(it1.__next__())
# StopIteration
