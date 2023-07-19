import re

# pattern = re.compile('(?P<v>\d+)')
# text = 'ht966ln10vt11ff12cr13'
# print(re.match(pattern, text))
# # None
# m = re.search(pattern, text)
# print(m)
# print(m.span())
# print(m.start())
# print(m.end())
# print(m.group())
# print(m.groupdict())
# # <re.Match object; span=(2, 3), match='9'>
# print(m.expand('\g<v>'))
# # 966


# 定义正则表达式模式
pattern = r'(\d{4})-(\d{2})-(?P<day>\d{2})'
# 定义模板字符串
template = r'Year: \1, Month: \2, Day: \g<day>'

# 输入待匹配的字符串
date_str = '2023-07-04'

# 执行正则匹配
match = re.match(pattern, date_str)
if match:
    # 使用expand方法进行替换
    result = match.expand(template)
    print(result)
else:
    print("No match found.")
