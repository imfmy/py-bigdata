import string

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
# 两个可迭代对象构造字典
full_half_dictx = {k: v for k, v in full_half}
print(full_half_dictx)
full_half_dict = {k: v for k, v in zip([e for e in full_width], [h for h in half_width])}
print(type(full_half_dict),full_half_dict)
print(format(ord('　'), '#x'))
print('a' < 'b' < 'c')
print('\t' < '\n')
print(' ' == '\x20' == '\u0020')
print(ord('['), ord('［'), ord('【'), ord('【'), )


def full2half(str1):
    for c in str1:
        # if format(ord(c), '#x') != '0x3000' and 'ff01' <= format(ord(c), '#x') <= '0xff5e':
        if c in full_half_dict.keys():
            for k, v in full_half_dict.items():
                if c == k:
                    str1 = str1.replace(k, v)
    return str1


print(full2half('（'))