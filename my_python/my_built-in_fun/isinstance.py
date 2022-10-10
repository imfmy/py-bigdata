print(isinstance(1, int))
# True
print(isinstance('1', (int, float, bool)))
# False
print(isinstance('1', (int, str)))
# True
print(isinstance([1, 2, 3], (dict, tuple)))
# False
print(isinstance((1, 2), (dict, tuple)))
# True
