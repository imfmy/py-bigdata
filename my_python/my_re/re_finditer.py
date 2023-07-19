import re

# def finditer(pattern: bytes | Pattern[bytes],
#              string: bytes | bytearray | memoryview | array | mmap,
#              flags: int | RegexFlag = ...) -> Iterator[Match[bytes]]
# Return an iterator over all non-overlapping matches in the string.
# For each match, the iterator returns a Match object.  Empty matches are included in the result.

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
# ['foot', 'fell', 'fastest']
it1 = re.finditer(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(it1, list(it1),sep='\n')
# <callable_iterator object at 0x000001AB4E5F4F10>
# [<re.Match object; span=(6, 10), match='foot'>, <re.Match object; span=(19, 23), match='fell'>, <re.Match object; span=(24, 31), match='fastest'>]


print(re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10 and long='))
# [('width', '20'), ('height', '10')]
print(re.findall(r'(\w+)=(\d*)', 'set width=20 and height=10 and long='))
# [('width', '20'), ('height', '10'), ('long', '')]
print(re.findall(r'(?:\w+)=(\d+)', 'set width=20 and height=10'))
# ['20', '10']
print(re.findall(r'(\w+)=(?=\d+)', 'set width=20 and height=10 hi'))
# ['width', 'height']
print(re.findall(r'b', 'a'))
# []
text2 = 'abc1234#你好啊&*……asdf'
print(re.findall('[\u4e00-\u9fa5]+', 'abc1234#你好啊&*……a我不好sdf'))
# ['你好啊', '我不好']
text2 = '1a 2b 14m'
print(re.findall(r'(\d+)([a-z]+)', text2))
# [('1', 'a'), ('2', 'b'), ('14', 'm')]
it = re.finditer(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(it, type(it))
# <callable_iterator object at 0x0000021EFED4BB50> <class 'callable_iterator'>
for i in it:
    print(i, type(i))
    print(i.group())
    print(i.groups())

it = re.finditer(r'(\w+)=(\d+)', 'set width=20 and height=10')
for i in it:
    print(i.groups(), i.group(), i.group(1), i.group(2))
# ('width', '20') width=20 width 20
# ('height', '10') height=10 height 10
