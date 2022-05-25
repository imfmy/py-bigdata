print(0xff01)
# 中文标点不一定是全角，如以下就是非全角的中文符号
print(hex(ord('￥')), hex(ord('…')), hex(ord('—')), hex(ord('、')), hex(ord('【')), hex(ord('】')),
      hex(ord('‘')), hex(ord('＇')), hex(ord('“')), hex(ord('。')), hex(ord('》'), ), hex(ord('《'))
      )
# 中文标点部分是全角，如以下
print(hex(ord('！')), hex(ord('，')),hex(ord('（')))
# 全角也不一定是中文符号
print(hex(ord('＇')),hex(ord('＂')))

print(hex(ord('〕')))
