import re

pattern = re.compile('(?P<v>\d+)')
text = 'ht966ln10vt11ff12cr13'
print(re.match(pattern, text))
# None
m = re.search(pattern, text)
print(m)
# <re.Match object; span=(2, 3), match='9'>
print(m.expand('\g<v>'))
# 966
