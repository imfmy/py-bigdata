# dk = ['a', 'b', 'c']
# dv = [1, 2, 3]
# dk = 'abc'
# dv = [1, 2, 3]
dk = ('a', 'b', 'c')
dv = (1, 2, 3)
# 字典生成
dict1 = {k: v for k, v in zip([x for x in dk], [y for y in dv])}
print(dict1)
# {'a': 1, 'b': 2, 'c': 3}
dict2 = {k: v for k, v in zip(dk, dv)}
print(dict2)
# {'a': 1, 'b': 2, 'c': 3}

