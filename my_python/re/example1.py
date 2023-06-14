import re

sql = """chg1 AS ( SELECT -- 非业务字段
                        update_date, use_status, is_final, l.id,
                        -- 主键字段
                        ${PK_FIELDS},
                        -- pg非主键业务字段
                        ${PG_NPK_FIELDS}
                        -- 其他业务字段
                        ${OTHER_FIELDS}
                   FROM chg          l
                       LEFT JOIN ( SELECT id, ${OTHER_FIELDS}
                                     FROM yst
                                    WHERE use_status = 1
                                   ) r
                                 ON chg.id = r.id
                 )"""
print(sql)
p1 = re.compile(r'FROM chg(.*?ON chg.id = r.id)', re.S)
mo1 = re.search(p1, sql)
print(mo1)
print('22', mo1.group(1))
print(re.sub(p1, 'FROM chg ', sql))
