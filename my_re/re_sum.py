import re



# abc1234#你好啊&*……asdf
text2 = 'abc1234#你好啊&*……asdf'


def f1(m1):
    v = m1.group('v')
    return str(int(v) * 2)


print(re.sub('(?P<v>\d+)', f1, text2))
