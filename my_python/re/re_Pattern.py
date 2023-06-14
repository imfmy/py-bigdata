import re

# 正向后视
m1 = re.search('(?<=ab)cd', 'cdab')
if m1:
    print(m1.group())
else:
    print('没有匹配到')
    # 没有匹配到
m2 = re.search('(?<=ab)cd', 'abcd')
if m2:
    print(m2.group())
else:
    print('没有匹配到')
    # cd
m3 = re.search('(?<=-)\w+', 'app-qcc-bbq')
if m3:
    print(m3.group())
# qcc
l1 = ['<user@host.com>', 'user@host.com', 'user@host.com>', '<user@host.com']
for str1 in l1:
    m = re.search('(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)', str1)
    i = l1.index(str1)
    if m:
        print(i, ':')
    else:
        print(i, ':', '没匹配到')
m = re.search('(<)?(\w+@\w+(?:\.\w+)+)(?(1)(>)|($))', l1[0])
print(m)
print(m.group())
print(m.groups())
print(m.group(1), m.group(2), )

print(re.search('\w+', 'a1_你她'),)
print(re.search('([a-zA-Z_])+', 'a1_你她'))
