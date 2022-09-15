# //print(eval('x+1'))
# NameError: name 'x' is not defined
print(exec('print(x+1)', {'x': 1}))
# 2
# None