import re

pn = re.compile('\d+', 0)
m = pn.search('a97b98$asdf')
print(m)
# <re.Match object; span=(1, 3), match='97'>
print(pn.search('a97b98$asdf', 0, 5))
# <re.Match object; span=(1, 3), match='97'>
print(pn.search('a97b98$asdf'[0:5], 0))
# <re.Match object; span=(1, 3), match='97'>