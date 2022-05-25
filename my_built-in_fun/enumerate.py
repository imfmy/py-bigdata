l = ['Sprint', 'Summer', 'Fall', 'Winter']
enu1 = enumerate(l)
print(enu1, type(enu1))
# <enumerate object at 0x000001BC5C563BC0> <class 'enumerate'>
for i in enu1:
    print(i)
    # (0, 'Sprint')
    # (1, 'Summer')
    # (2, 'Fall')
    # (3, 'Winter')
enu2 = enumerate(l, 2)
print(list(enu2))


# [(2, 'Sprint'), (3, 'Summer'), (4, 'Fall'), (5, 'Winter')]

def enu(sequence, start=0) -> enumerate:
    n = start
    for e in sequence:
        yield (n, e)
        n += 1


print(enu(l, 5))
# <generator object enu at 0x0000016F37C7BAC0>
