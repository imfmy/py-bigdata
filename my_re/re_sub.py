import re

# def sub(pattern: Pattern[AnyStr],
#         repl: (Match[AnyStr]) -> AnyStr,
#         string: AnyStr,
#         count: int = ...,
#         flags: int | RegexFlag = ...) -> AnyStr
text1 = 'hello 世界! @张三a,123你,$*（中括）,h3'
# 将aeiou删除掉
print(re.sub(r'[aeiou]', '', text1, 0, 0))
# hll 世界! @张三,123你,$*（中括）,h3

# 删去字母
print(re.sub(r'[a-z]', '', text1))
#  世界! @张三,123你,$*（中括）,3

# 删除后的汉字
text2 = 'abc1234#你好啊&*……asdf'
re.findall('[\u4e00-\u9fa5]', 'abc1234#你好啊&*……asdf')
print(re.sub('(?<=#)[\u4e00-\u9fa5]+', '', text2))

# abc1234#你好啊&*……asdf
text2 = 'abc1234#你好啊&*……asdf'


def f1(m1):
    v = m1.group('v')
    return str(int(v) * 2)


print(re.sub('(?P<v>\d+)', f1, text2))

s1 = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
            r'static PyObject*\npy_\1(void)\n{',
            'def myfunc():')
print(s1)
# static PyObject*
# py_myfunc(void)
# {
s2 = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
            r'static PyObject*\npy_\g<1>(void)\n{',
            'def myfunc():')
print(s2)
# static PyObject*
# py_myfunc(void)
# {
def dashrepl(matchobj):
    if matchobj.group(0) == '-':
        return ' '
    else:
        return '-'
r1 = re.sub('-{1,2}', dashrepl, 'pro----gram-files')
print(r1)
# pro--gram files
print(re.sub('x*', '-', 'abxd'))
# -a-b--d-
print(re.subn('x*', '-', 'abxd'))
# ('-a-b--d-', 5)