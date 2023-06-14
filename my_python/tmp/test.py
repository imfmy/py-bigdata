import json

# max_merge_by('xxx',priority,union_cols=None)
s1 = '[{"c1":2,"qz":4},{"c1":0,"c2":"a","c3":[1,3],"qz":0},{"c1":23,"c2":"y","c3":[6],"qz":2},{"c1":11,"c2":"b","qz":3},{"c1":1,"c2":"x","c3":[1,5],"qz":1}] '
js = json.loads(s1)
# for e in js:
# [{"c1":2,"qz":4},
# {"c1":0,"c2":"a","c3":[1,3],"qz":0},
# {"c1":23,"c2":"y","c3":[6],"qz":2},
# {"c1":11,"c2":"b","qz":3},
# {"c1":1,"c2":"x","c3":[1,5],"qz":1}]
union_cols = 'c3'.split(',')
col_names = ["c1", "c2", "c3", "qz"]
res = js[0]
i = 1
while i < len(js):
    for col in col_names:
        # 如果遍历的字段有值
        if js[i].get(col, None):
            # 如果字段需要去重合并（忽略权重），则直接去重合并
            if col in union_cols:
                if col not in res:
                    res[col] = []
                res[col] = list(set(res[col] + js[i][col]))
            # 否则按优先级取非空值
            else:
                # 如果遍历的字段权重大或res的字段为空时
                if js[i]['qz'] > res['qz'] or not res.get(col, None):
                    res[col] = js[i][col]
    i = i + 1
print(res)
