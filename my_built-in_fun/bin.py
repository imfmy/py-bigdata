# -*- coding: utf-8 -*-
# def bin(__number: int | SupportsIndex) -> str
print(bin(11))  # 0b1011
print(bin(0x11))  # 0b10001
print(bin(0o11))  # 0b1001
print(bin(0b11))  # 0b11
print(bin(-10))  # -0b1010
print(format(10, '#b'), format(10, 'b'))
# 0b1010 1010
print(f'{10:#b}', f'{10:b}')
# 0b1010 1010
# 0b1010 1010
print(f'{10:#o},{10:#x}', f'{10:o}' == format(10, 'o'))
# 0o12,0xa True
print(bool('s'))