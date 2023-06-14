import re

text = 'ht9ln10A65中文？#1'
pn = re.compile('(\d+)([a-z]+)10([A-Z]+)65(?P<v>[\u4e00-\u9fa5]+)')
m = re.search(pn, text)
print(m)
# <re.Match object; span=(2, 12), match='9ln10A65中文'>
print(m.groups(), m.group(0), m.group())
# ('9', 'ln', 'A', '中文') 9ln10A65中文 9ln10A65中文
print(m.group(1, 2, 4, 3))
# ('9', 'ln', '中文', 'A')
print(m.group('v', 1))
# ('中文', '9')