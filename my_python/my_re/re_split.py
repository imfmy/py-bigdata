import re

# def split(pattern: Pattern[AnyStr],
#           string: AnyStr,
#           maxsplit: int = ...,
#           flags: int | RegexFlag = ...) -> list[AnyStr]

print(re.split('\W+', 'a, b,c你好，1d，&*（'))
# ['a', 'b', 'c你好', '1d', '']
print(re.split('\W+', 'a, b,c你好，1d，&*（', 0, 0))
# ['a', 'b', 'c你好', '1d', '']
print(re.split('\W+', 'a, b,c你好，1d，&*（', 0, re.ASCII))
# ['a', 'b', 'c', '1d', '']
print(re.split('\W+', 'a, b,c你好，1d，&*（', 2, re.ASCII))
# ['a', 'b', 'c你好，1d，&*（']
print(re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE))
# ['0', '3', '9']
# 如果分隔符里有捕获组合，并且匹配到字符串的开始，那么结果将会以一个空字符串开始。对于结尾也是一样
print(re.split(r'(\W+)', '#a, b!c你好&*（'))
# ['', '#', 'a', ', ', 'b', '!', 'c你好', '&*（', '']
print(re.split(r'\W*', '#a, b!c你好&*（'))
# ['', '', 'a', '', 'b', '', 'c', '你', '好', '', '']
# 样式的空匹配仅在与前一个空匹配不相邻时才会拆分字符串。
print(re.split(r'\b', 'Words,|...words,- words.'))
# ['', 'Words', ',|...', 'words', ',- ', 'words', '.']
# //print(re.split(r'\b+', 'Words,|...words,- words.'))
# re.error: nothing to repeat at position 2
