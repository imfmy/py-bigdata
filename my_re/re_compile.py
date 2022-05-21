import re

# def compile(pattern: Pattern[AnyStr],
#             flags: int | RegexFlag = ...) -> Pattern[AnyStr]
pattern = re.compile(r'\d+')
print(pattern, type(pattern))
# re.compile('\\d+') <class 're.Pattern'>
pattern.match('hao1234%.你好++')
