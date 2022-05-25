from pypinyin import pinyin, lazy_pinyin, Style
import re


def get_lower_initials(ent_name) -> str:
    """获取字符串中汉字的首字母
        '#$%^一1单城（有限合伙）abc123@' -> 'yydcyxhhabcyes'
    """
    r = re.sub('[^\u4e00-\u9fa5a-zA-Z0-9]', '', ent_name)
    r1 = re.sub(r'\d+', num_letter, r)
    r2 = lazy_pinyin(r1, Style.FIRST_LETTER)
    return ''.join(r2)


def num_letter(m):
    nl_dict = {'0': 'l', '1': 'y', '2': 'e', '3': 's', '4': 's',
               '5': 'w', '6': 'l', '7': 'q', '8': 'b', '9': 'j'}
    s = m.group()
    for k, v in nl_dict.items():
        s = s.replace(k, v)
    return s


text = '#$%^一1单城（有限合伙）abc123@'
print(get_lower_initials(text))
# print(get_lower_initials(text))
# print(lazy_pinyin('你好☆☆a', errors=lambda x: oth(x)))
with open('../my_re/regexp.txt', encoding='utf-8') as fo:
    contents = fo.read()

r = re.sub('[^\u4e00-\u9fa5a-zA-Z0-9]', '', contents)
print(r)
r1 = re.sub(r'\d+', num_letter, r)
print(r1)
r2 = lazy_pinyin(r1, Style.FIRST_LETTER)
print(''.join(r2))

print(get_lower_initials('89 81'))
print(re.search('\d+','abc'))
