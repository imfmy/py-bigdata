print(int(True))
# 1
print(int(False))
# 0
print(int(0.111))
# 0
print(int(3.1416))
# 3
print(int(9.9))
# 9
print(int('123'))
# 123
# print(int('hello'))
# # ValueError: invalid literal for int() with base 10: 'hello'
# print(int(None))
# # TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
print(int())
# 0