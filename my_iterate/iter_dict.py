m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
     'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
for k in m:
    print(k, m[k])
    # Jan 1
    # Feb 2
    # ...
    # 注意从 Python 3.7 开始，字典的遍历顺序一定和输入顺序一样。先前的版本并没有明确这一点，所以不同的实现可能不一致。
for k, v in m.items():
    print(k, v)
    # Jan 1
    # Feb 2
    # ...
l: list = [('a', 97), ('b', 98), ('c', 99)]
d = dict(iter(l))
print(d, type(d))
# {'a': 97, 'b': 98, 'c': 99} <class 'dict'>
d1 = dict(l)
print(d1, type(d))
# {'a': 97, 'b': 98, 'c': 99} <class 'dict'>

with open('./for_line.txt.py', encoding='utf-8') as of:
    print(of,type(of))
    for line in of:
        print(line)
