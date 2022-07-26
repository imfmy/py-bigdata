import string

print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters, len(string.ascii_letters), sep=' -- ')
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -- 52
print(string.digits, len(string.digits), sep=' -- ')
# 0123456789 -- 10
print(string.octdigits)
# 01234567
print(string.hexdigits)
# 0123456789abcdefABCDEF
print(string.punctuation, len(string.punctuation), sep=' -- ')
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ -- 32
t1 = string.punctuation
s1 = '`~!@#$%^&*()_+=-\\|}{][;:/?.>,<\'\"'
print(len(s1))
for i in s1:
    if string.punctuation.find(i) != -1:
        print((i, t1.find(i)))
    else:
        print(f'{i}不存在string.punctuation中')
print('-->' + string.printable + '<--', len(string.printable))
# -->0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# <-- 100
s = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
print('-->' + s + '<--', len(s))
# -->0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~<-- 94

# 查找s中不在string.printable的字符及其ascii值
for i in string.printable:
    if i not in s:
        print(('\'' + i + '\'', ord(i)))
# ("' '", 32)
# ("'\t'", 9)
# ("'\n'", 10)
# ("'\r'", 13)
# ("'\x0b'", 11)
# ("'\x0c'", 12)
for i in string.whitespace:
    print(('\'' + i + '\'', ord(i)))
# ("' '", 32) ## 空格
# ("'\t'", 9) ## 制表符
# ("'\n'", 10) ## 换行符
# ("'\r'", 13) ## 回车符
# ("'\x0b'", 11) ##\v 垂直制表符
# ("'\x0c'", 12) ##\f 换页
print(
    string.printable == string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.whitespace)
# True

half_width = '\x20' + string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.digits
full_width = '\u3000' + ''.join(chr(ord(i) + 65248) for i in half_width[1:96])
print(half_width, len(half_width), sep=' --')
print(full_width, len(full_width), sep=' --')
print([e for e in full_width], len([e for e in full_width]))
print('\x20', '\u3000')
full_half = zip([e for e in full_width], [h for h in half_width])
print(full_half)
full_half_list = list(full_half)
print(full_half_list)
full_half_dict = {k:v for k,v in zip([e for e in full_width], [h for h in half_width])}
print(full_half_dict)
print(format(ord('　'), '#x'))
print('a' < 'b' < 'c')
print('\t' < '\n')


def full2half(str1):
    for c in str1:
        for k, v in full_half_list:
            # if format(ord(c), '#x') != '0x3000' and 'ff01' <= format(ord(c), '#x') <= '0xff5e':
            # if c in full_half_list
                str1 = str1.replace()


print(0xff00)
