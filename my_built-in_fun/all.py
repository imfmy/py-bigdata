a = '12345'
print(all(a), all('0'), all(''))
# True True True
print(all([0, 1, 2, 3, 4, 5]))
# False
it1 = [True, True]
print(all(it1))
it1.append(False)
print(it1, all(it1), all([]))
# [True, True, False] False True
