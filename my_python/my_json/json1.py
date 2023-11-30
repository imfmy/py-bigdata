import json

# 对基本的 Python 对象层次结构进行编码

l1 = ['e1', {'k': ('t1', None, 1.0, 2)}]
print(l1, type(l1))
# ['e1', {'k': ('t1', None, 1.0, 2)}] <class 'list'>

print(json.dumps(l1), type(json.dumps(l1)))
# ["e1", {"k": ["t1", null, 1.0, 2]}] <class 'str'>
print(json.dumps(''))
# ""

str1 = "\"foo\bar"
str2 = '\"foo\bar'
str3 = '\"foar'
print(str1, str2, str3, str1 == str2, str2 == str3)
# "foar "foar "foar True False
print(json.dumps(str1), json.dumps(str1)[0], sep='|')
# "\"foo\bar"|"
print(json.dumps(str2))
# "\"foo\bar"
print(json.dumps(1))
# 1

print('\u9999', json.dumps('\u9999'), r'\u9999',json.dumps('\u9999',ensure_ascii=False))
# 香 "\u9999" \u9999 "香"

# #默认sort_keys=False不会对key排序
print(json.dumps({"c": 0, "b": 2, "a": 0}, sort_keys=True))
# {"a": 0, "b": 0, "c": 0}

str3 = '你好abc'
# #默认ensure_ascii=True是以ascii码形式显示字符（中文会以Unicode编码展示）
print(json.dumps(str3), json.dumps(str3, ensure_ascii=False), sep='|')
# "\u4f60\u597dabc"|"你好abc"
# 紧凑编码
l2 = [1, 2, 3, {'4': 5, '6': 7}]
print(l2)
# [1, 2, 3, {'4': 5, '6': 7}]
print(json.dumps(l2, separators=(',', '->')))
# [1,2,3,{"4"->5,"6"->7}]

# 美化输出:
print(json.dumps({'a': 97, 'A': 65, 'c': '99'}, sort_keys=False, indent=4, separators=(',', ':')))
# {
#     "a":97,
#     "A":65,
#     "c":"99"
# }

# JSON解码:
s1 = '[1,2,{"3":4,"5":6}]'
print(s1, type(s1))
# [1,2,{"3":4,"5":6}] <class 'str'>
j1 = json.loads(s1)
print(j1, type(j1))
# [1, 2, {'3': 4, '5': 6}] <class 'list'>
s2 = '"\\"foo\\bar"'
print('57:', s2, json.loads(s2), sep='|')
# 57:|"\"foo\bar"|"foar
print('\u4e00-\u9fa5', hex(ord('龥')))
# 一-龥 0x9fa5

l = [5, 1, 2]
print(json.dumps(l, sort_keys=True))  # sort_keys仅对字典有效
# [5, 1, 2]
print(json.dumps(l, indent=4, separators=('#', '@')))
# [
#     5#
#     1#
#     2
# ]
# ]
print(json.dumps(l, indent='aa', separators=(', ', ': ')))
# [
# aa5,
# aa1,
# aa2
# ]
