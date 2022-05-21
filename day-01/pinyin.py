from pypinyin import pinyin, lazy_pinyin, Style
import xpinyin
import re

p = xpinyin.Pinyin()
str1 = '南京（有限合伙）#$%^%！@'
s = p.get_initials(str1, '').lower()
print(s)
# nj（yxhh）#$%^%！@
re.match('abc', 'abcd')
# (0, 3)
print(re.match('www', 'www.runoob.com,www').span())
# (0, 3)
print(re.match('com', 'www.runoob.com'))
# None # re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败 函数返回 None
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
print(matchObj)
# <re.Match object; span=(0, 26), match='Cats are smarter than dogs'>
print(matchObj.group(), '|', matchObj.group(0))
# Cats are smarter than dogs | Cats are smarter than dogs
print(matchObj.groups())
# ('Cats', 'smarter')
print(matchObj.span(1))
# (0, 4)
print(matchObj.group(1) + '|')
# Cats|
print(matchObj.span(2))
# (9, 16)
print(matchObj.group(2))
# smarter
# re.search 匹配整个字符串，直到找到第一个匹配终止
print(re.search('www', 'runoob.com,WWW'), re.search('www', 'runoob.com,WWWW', re.I))
# None <re.Match object; span=(11, 14), match='WWW'> # re.I忽略大小写
print(re.search('www', 'www.runoob.com,www'))
# <re.Match object; span=(0, 3), match='www'>
print(re.search('www', 'www.runoob.com').span())
# (0, 3)
print(re.search('com', 'www.runoob.com').span())
# (11, 14)
print(re.search(r'[^a-z]', 'nj（yxhh）#$%^%！@'))
# <re.Match object; span=(2, 3), match='（'>
# 把所有不是小写字母的字符替换为空字符''
print(re.sub(r'[^a-z]', '', 'nj（yxhh）#$%^%！@', 0, 0))
# njyxhh
phone = "2004-959-559 # 这是一个电话号码"
print(re.sub(r' #.*$', "", phone) + '|')


# 2004-959-559|

def double(matched):
    value = int(matched.group('g1'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<g1>\d+)', double, s))
print(re.sub('(?P<g1>\d+?)', double, s, 2))
# A46G8HFD1134
s1 = '南京（有限合伙）#$%^%asdfa！@'
r1 = re.sub(r'[^(\u4e00-\u9fa5)]', '', s1)
print(r1)
# 南京有限合伙
r2 = pinyin(r1, Style.FIRST_LETTER)
print(r2)
# [['n'], ['j'], ['y'], ['x'], ['h'], ['h']]
r3 = lazy_pinyin(r1, style=Style.FIRST_LETTER)
print(''.join(r3))
# njyxhh
print(''.join(lazy_pinyin(s1, Style.FIRST_LETTER, errors='ignore')))
# njyxhh

def get_lower_initials(col) -> str:
    return ''.join(lazy_pinyin(col, Style.FIRST_LETTER, errors='ignore'))
print(get_lower_initials(s1))  # njyxhh