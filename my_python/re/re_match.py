import re

str1 = """hello啊
world"""
# 判断整个字符串是否全部由非中文组成
print(str1)
res = re.fullmatch(r'^[^\u4e00-\u9fa5]+$', str1, flags=0)
print(re.fullmatch(r'^[^\u4e00-\u9fa5]+$', '', flags=0))

print(re.fullmatch(r'[\d.]+', '12.32'))
print('>', '药材 '.strip(), '<', sep='|')
# >|药材|<
print('1 药材 '.split(' '))
print(hex(ord(' ')))
print('\\u00a0')