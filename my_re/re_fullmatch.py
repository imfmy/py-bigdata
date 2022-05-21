import re
# def match(pattern: Pattern[AnyStr],
#           string: AnyStr,
#           flags: int | RegexFlag = ...) -> Match[AnyStr] | None
text1 = 'hello 世界! @张三a,123你,$*（中括）,h3'
m1 = re.match('hello', text1)
print(m1, '|', type(m1))  # 匹配成功，返回一个匹配的对象
# <re.Match object; span=(0, 5), match='hello'> | <class 're.Match'>
# //s1 = m1.span(1)
# IndexError: no such group
s1 = m1.span()
print(s1, type(s1), m1.span() == m1.span(0))
# (0, 5) <class 'tuple'> True
g1 = m1.group()
print(g1, type(g1), m1.group() == m1.group(0))
# hello <class 'str'> True
# //g2 = m1.group(1) # IndexError: no such group
print(m1.groups(), type(m1.groups()))
# () <class 'tuple'>
m2 = re.match('(he)(llo)', text1)
print(m2.span(), m2.span(0), m2.span(1), m2.span(2))
# (0, 5) (0, 5) (0, 2) (2, 5)
print(m2.groups(), m2.group(0), m2.group(), m2.group(1), m2.group(2))
# ('he', 'llo') hello hello he
m3 = re.match('(123)', text1)
print(m3)  # None