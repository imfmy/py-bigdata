# //print(eval('x+1'))
# NameError: name 'x' is not defined
print(eval('x+1', {'x': 1}))
# 2
