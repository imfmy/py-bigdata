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
print(m[0], m[1], m[2], m[3], m[4], m['v'])
# 9ln10A65中文 9 ln A 中文 中文
print(m.groupdict())
# {'v': '中文'}

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.groupdict(), m.groups())
# {'first_name': 'Malcolm', 'last_name': 'Reynolds'} ('Malcolm', 'Reynolds')
print(m[1], m[2], m['first_name'], m['last_name'])
# Malcolm Reynolds Malcolm Reynolds

m = re.match(r"(..)+", "a1b2c3")
print(m.group(1))
# c3
m = re.match(r"(..)", "a1b2c3")
print(m.group(1))
# a1
m = re.match(r"(..){2}", "a1b2c3")
print(m.group(1))
# b2

m = re.match(r"(\d+)\.?(\d+)?", "24")
print(m.groups(), m.groups('0'))
# ('24', None) ('24', '0')


email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
print(email[:m.start()] + email[m.end():])
# tony@tiger.net