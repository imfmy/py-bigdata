import re

# def sub(pattern: Pattern[AnyStr],
#         repl: (Match[AnyStr]) -> AnyStr,
#         string: AnyStr,
#         count: int = ...,
#         flags: int | RegexFlag = ...) -> AnyStr

text = '123abc123xyz'
ptn = re.compile(r'Abc', re.IGNORECASE)
print(re.sub(ptn, '#', text))
# 123#123xyz
print(re.sub('Abc', '@', text, re.IGNORECASE))
# 123abc123xyz


text2 = '123abc()123xyz'
ptn = re.compile(re.escape('abc()'))
ptn = re.compile(fr'abc{re.escape("()")}')
print(ptn)
print(re.sub(ptn,'#',text2))
