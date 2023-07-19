import re

text = '你abc我123哈哈哈'
m = re.search(r'([a-z]+)我(\d+)', text)
print(f'match_object: {m}')
# All the subgroups
print(m.groups())
# ('abc', '123')

# The entire match
print(m.group(0))
# abc我123

# defaults to zero, the entire match's span.
print(m.span(), m.span(0))
# (1, 8) (1, 8)

# the subgroup1's span
print(m.span(1))
# (1, 4)
