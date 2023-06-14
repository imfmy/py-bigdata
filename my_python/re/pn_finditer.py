import re

pattern = re.compile('\d+')
text = 'ht9ln10vt11ff12cr13'
it = pattern.finditer(text)
print(it, type(it))
# <callable_iterator object at 0x000002465CD91E20> <class 'callable_iterator'>
for i in it:
    print(i)
# <re.Match object; span=(2, 3), match='9'>
# <re.Match object; span=(5, 7), match='10'>
# <re.Match object; span=(9, 11), match='11'>
# <re.Match object; span=(13, 15), match='12'>
# <re.Match object; span=(17, 19), match='13'>
it1 = pattern.finditer(text, 3, 10)
it2 = pattern.finditer(text[3:10])
print()
p = re.compile('(\d+[a-z]+)', re.I)
it = p.finditer(text, 0)
for i in it:
    print(i)
# <re.Match object; span=(2, 5), match='9ln'>
# <re.Match object; span=(5, 9), match='10vt'>
# <re.Match object; span=(9, 13), match='11ff'>
# <re.Match object; span=(13, 17), match='12cr'>

print()
p = re.compile('(\d+)([a-z]+)', re.I)
it = p.finditer(text)
for i in it:
    print(i)
    print(i.group(), i.groups(), i.group(1), i.group(2))
# <re.Match object; span=(2, 5), match='9ln'>
# 9ln ('9', 'ln') 9 ln
# <re.Match object; span=(5, 9), match='10vt'>
# 10vt ('10', 'vt') 10 vt
# <re.Match object; span=(9, 13), match='11ff'>
# 11ff ('11', 'ff') 11 ff
# <re.Match object; span=(13, 17), match='12cr'>
# 12cr ('12', 'cr') 12 cr