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

"""正则：只匹配前面的key（由字母或汉字组成）不匹配后面的值（有小数或整数组成）"""
text2 = '{"afterSaleRating": "5.0", "logisticsRating": "5.0", "synRating": "5.0", "userRating": "5.0"}'
print(re.findall(r'(?<!: )"([\u4e00-\u9fa5a-zA-Z]+?)"(?!,)', text2))
# ['afterSaleRating', 'logisticsRating', 'synRating', 'userRating']
it2 = re.finditer(r'(?<!: )"([\u4e00-\u9fa5a-zA-Z]+?)"(?!,)', text2)
for i in it2:
    print(i, type(i), i.group(0), i.groups(), sep='|')
