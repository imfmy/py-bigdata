import datetime

# 当前时间
now = datetime.datetime.now()
print(now)
# 2023-11-30 17:50:38.897348

# 格式化后的当前时间
fnow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(fnow)
# 2023-11-30 17:50:38

fnow1 = datetime.datetime.now().strftime('%Y%m%d')
print(fnow1)
# 20231130

today = datetime.datetime.today()
yst = today - datetime.timedelta(days=1)
print(yst)
# 2023-11-29 17:55:00.329561

tmr = today + datetime.timedelta(days=1)
print(tmr)
# 2023-12-01 17:55:33.126024
