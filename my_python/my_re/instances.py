import re

text = "He was carefully disguised but captured quickly by police."
print(re.findall(r"\w+ly\b", text))
# ['carefully', 'quickly']
text = "He was carefully disguised but captured quickly by police."
for m in re.finditer(r"\w+ly\b", text):
    print(m)
    print(m.group(), m.start(), m.end(), m.groups())
print(re.match(r"\W(.)\1\W", " ff "))
# <re.Match object; span=(0, 4), match=' ff '>
print(re.match("\\W(.)\\1\\W", " ff "))
# <re.Match object; span=(0, 4), match=' ff '>
print(r'\\')

