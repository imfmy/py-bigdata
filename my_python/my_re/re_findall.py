import re

# def findall(pattern: Pattern[AnyStr],
#             string: AnyStr,
#             flags: int | RegexFlag = ...) -> list
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
# ['foot', 'fell', 'fastest']
print(re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10'))
# [('width', '20'), ('height', '10')]
print(re.findall(r'(?:\w+)=(\d+)', 'set width=20 and height=10'))
# ['20', '10']
print(re.findall(r'(\w+)=(?=\d+)', 'set width=20 and height=10 hi'))
# ['width', 'height']

text2 = 'abc1234#你好啊&*……asdf'
print(re.findall('[\u4e00-\u9fa5]+', 'abc1234#你好啊&*……asdf'))

text2 = '1a 2b 14m'
print(re.findall(r'(\d+)([a-z]+)', text2))
# [('1', 'a'), ('2', 'b'), ('14', 'm')]
re_it = re.finditer(r'(\d+)([a-z]+)', text2)
print([i.groups() for i in re_it])
# [('1', 'a'), ('2', 'b'), ('14', 'm')]
