import re
import string

print(re.escape('https://www.python.org'))
# https://www\.python\.org
print(re.escape('()[]\|^$-.{}*+?'), re.escape('<>/'))
# \(\)\[\]\\\|\^\$\-\.\{\}\*\+\? <>/
print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
print(string.digits)
# 0123456789
legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
print(re.escape(legal_chars))
#  !\#\$%\&'\*\+\-\.\^_`\|\~:
operators = ['+', '-', '*', '/', '**']
s_o = sorted(operators, reverse=True)
print(s_o)
# ['/', '-', '+', '**', '*']
print('|'.join(map(re.escape, s_o)))
# /|\-|\+|\*\*|\*

digits_re = r'\d+'
sample = '/usr/sbin/sendmail - 0 errors, 12 warnings'
rp1 = digits_re.replace('\\', r'\\')
rp2 = digits_re.replace('\\', '\\\\')
print(rp1 == rp2, rp1)
# True \\d+
print(re.sub(digits_re, rp1, sample))
# /usr/sbin/sendmail - \d+ errors, \d+ warnings
re.purge()