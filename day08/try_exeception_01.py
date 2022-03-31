# print(5/0)
# print('end')
# # ZeroDivisionError: division by zero
try:
    print(5/1)
    print('try end!')
except ZeroDivisionError:
    print('除数不能为0!')
else:
    print('如果try不抛异常,则执行此语句!')
print('end')
# 5.0
# try end!
# 如果try不抛异常,则执行此语句!
# end