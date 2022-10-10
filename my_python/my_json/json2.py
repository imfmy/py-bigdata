import json

print(json.loads('null'), type(json.loads('null')))
# None <class 'NoneType'>
print(json.loads('["a","b",null,"null"]'))
# ['a', 'b', None, 'null']

str1 = '{"发货速度":"4.42","商品描述":"3.92","服务质量":"4.63","店铺评分":"4.4"}'
# str2 = None
# print(json.loads(str2))
# TypeError: the JSON object must be str, bytes or bytearray, not NoneType
dt1 = json.loads(str1)
print(dt1, type(dt1), sep='||')
# {'发货速度': '4.42', '商品描述': '3.92', '服务质量': '4.63', '店铺评分': '4.4'}||<class 'dict'>
dt2 = {"a": "x", "b": "y", "c": "z"}
dt1 = {'a': 1, 'b': 2, 'c': 3, "d": 4}
print({dt2.get(k, k): v for k, v in dt1.items()})
