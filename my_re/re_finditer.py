import re

it = re.finditer(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(it, type(it))
# <callable_iterator object at 0x0000021EFED4BB50> <class 'callable_iterator'>
for i in it:
    print(i, type(i))
    print(i.group())
    print(i.groups())

it = re.finditer(r'(\w+)=(\d+)', 'set width=20 and height=10')
for i in it:
    print(i.groups(), i.group(), i.group(1), i.group(2))
# ('width', '20') width=20 width 20
# ('height', '10') height=10 height 10
