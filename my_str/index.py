# def get_lower_initials(ent_name) -> str:
#     """获取字符串中汉字的首字母
#         '南京（有限合伙）#$%^%asdfa！@' -> 'njyxhh'
#     """
#     ent_name_abbr = ''.join(lazy_pinyin(ent_name, Style.FIRST_LETTER, errors='ignore'))
#     return ent_name_abbr