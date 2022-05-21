import re

pattern = re.compile("o")
print(pattern.match('dog'))
# None
print(pattern.match('og'))
# <re.Match object; span=(0, 1), match='o'>