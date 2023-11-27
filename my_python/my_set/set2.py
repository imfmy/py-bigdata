import json
str1 = '{"用户评价":"8.33","物流时效":"7.32","售后服务":"9.70"}'
print(set(json.loads(str1).keys()),set(json.loads(str1)))
# {'售后服务', '物流时效', '用户评价'} {'售后服务', '物流时效', '用户评价'}
set0 = set()
set1 = {'x','a', 'b', 'c'}
set2 = set(['a', 'b', 'c'])
set3 = {'a', 'b', 'c', 'd'}
print(set1 == set2, set1 < set2, set1 <= set2, set1.issubset(set2), set2 > set1, set2 >= set1, set2.issuperset(set1))
# True False True True False True True
print(set0 == set1, set0 < set1, set0 <= set1, set0.issubset(set1), set1 > set0, set1 >= set0, set1.issuperset(set0))
# False True True True True True True
print(set2 == set3, set2 < set3, set2 <= set3, set2.issubset(set3), set3 > set2, set3 >= set2, set3.issuperset(set2))
# False True True True True True True
# print(None <= set1)
# TypeError: '<=' not supported between instances of 'NoneType' and 'set'
# print(set0.issuperset(None))
# TypeError: 'NoneType' object is not iterable
print(set2.intersection(set1))
print('inter_set ', set2.intersection({}), bool(set2.intersection({})))
