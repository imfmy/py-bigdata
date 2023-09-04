import json

s1 = '[{"qz":4},{"qz":2,"c1":"b"},{"qz":3,"c1":"c"},{"qz":1,"c1":"a"}]'
# res = {'c1':{3:"c",2:"b",1:"a"}
js = json.loads(s1)
is_merge = True
print(js)
d1 = {'c1': {}}
for col in js:
    qz = col.get('qz', None)
    v = col.get('c1', None)
    if qz and v:
        d1['c1'][qz] = v
print(d1)
if is_merge:
    res = []
    for k1, v1 in d1['c1'].items():
        if not isinstance(v1, list):
            v1 = [v1]
        res = list(set(res + v1))
else:
    res = d1['c1'][max(d1['c1'])]
print(json.dumps(res, ensure_ascii=False))
