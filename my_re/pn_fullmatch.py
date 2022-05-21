import re
pattern = re.compile('o')
print(pattern.fullmatch('og'))
# None
print(pattern.fullmatch('o'))
# <re.Match object; span=(0, 1), match='o'>