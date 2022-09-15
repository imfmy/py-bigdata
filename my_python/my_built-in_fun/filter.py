it = [1, 2, 3, 4]


def fun1(n):
    if n % 2 == 0:
        return n
    else:
        return False


fo = filter(fun1, it)
print(fo, type(fo))
# <filter object at 0x000002331DB3B430> <class 'filter'>
print(list(fo))
# [2, 4]
print(list(filter(None, it)))
# [1, 2, 3, 4]
