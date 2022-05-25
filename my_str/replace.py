import unicodedata

print(ord('（'),
      ord('〔'),
      f"{ord('（'):#x}",
      ord('（'))
print(10 > 0x10)
print(unicodedata.east_asian_width('１'))
print(unicodedata.east_asian_width('1'))
print(ord('（'), ord('〔'), ord('('))
# 65288 12308 40
print('（' == '〔' or '〔' == '(')
# False
print(f"{ord('%'):#x},{ord('〔'):#x}")
print(ord('％')-ord('%'))
print(ord('！')-ord('!'))
print(0x7e-0x20)