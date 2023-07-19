import json

# max_merge_by('xxx',priority,union_cols=None)
s1 = '[{"c1":2,"qz":4},{"c1":0,"c2":"a","c3":[1,23],"qz":0},{"c1":23,"c2":"y","c3":[6,5,6,6],"qz":2},{"c1":11,"c2":"b","qz":3},{"c1":1,"c2":"x","c3":[1,5],"qz":1}]'
# [{"c1":2,"qz":4},
# {"c1":0,"c2":"a","c3":[1,3],"qz":0},
# {"c1":23,"c2":"y","c3":[6],"qz":2},
# {"c1":11,"c2":"b","qz":3},
# {"c1":1,"c2":"x","c3":[1,5],"qz":1}]
js = json.loads(s1)
union_cols = 'c3,c1'.split(',')
# 取所有的字段名
cols = set(ee for e in js for ee in e)
# l1 = {"c1": {4: 2, 0: 0, 2: 23, 3: 11, 1: 1}, "c2": {4: 2, 0: 0, 2: 23, 3: 11, 1: 1}}
# print(l1["c1"][max(l1["c1"])])
d1 = {}
for line in js:
    i = 0
    for col in cols:
        if line.get(col, None) and line.get('qz', None):
            if col in d1:
                d1[col][line.get('qz')] = line[col]
            else:
                d1[col] = {}
                d1[col][line.get('qz')] = line[col]
# print(d1)
d2 = dict()
for k, v in d1.items():
    v1s = None
    if k in union_cols:
        v1s = []
        for k1, v1 in v.items():
            if not isinstance(v1, list):
                v1 = [v1]
            v1s = list(set(v1s + v1))
    else:
        v1s = v[max(v)]
    d2[k] = v1s
print(d2)
