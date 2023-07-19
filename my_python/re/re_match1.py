import re

str1 = 'abc \t \v \f  1234'
# 贪婪匹配
match1 = re.match(r'([^\d.]*)(\s*)([\d.]+)', str1)
print(match1, match1.group(1), match1.group(2),match1.group(3), sep='|')
# <re.Match object; span=(0, 15), match='abc \t \x0b \x0c  1234'>|abc 	    ||1234

# 非贪婪匹配
match2 = re.match(r'([^\d.]*?)(\s*)([\d.]+)', str1)
print(match2,match2.group(1),match2.group(2),match2.group(3),sep='|')
print(hex(ord('	')))