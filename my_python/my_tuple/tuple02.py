l1 = [
    [3, 'c', 'd'],
    [2, 'b', 'c'],
    [1, 'a', 'b']

]


for l in l1:
    for l2 in l1[1:len(l1)-1:1]:
        if l[2]==l2[1]:

