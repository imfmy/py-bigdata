import statistics

l1 = ['a', 'b']
l2 = ['a', 'b']
l3 = ['b', 'a']
print(l1 == l2, l2 == l3)
d1 = {'pid': ('string', None), 'update_date': ('bigint', ''), 'has_trade_show': ('boolean', '有无参展信息'),
      'trade_show_count': ('bigint', '展会数量'), 'trade_show_name': ('array<string>', '展会名称'),
      'trade_show_start_date': ('array<bigint>', '展会开始时间（嵌套类型）'), 'latest_trade_show_name_raw': ('string', '最近展会名称'),
      'latest_trade_show_start_time': ('string', '最近展会开始时间'), 'latest_trade_show_end_time': ('string', '最近展会结束时间')}
print(d1['trade_show_name'][0].startswith('array'))
array_fields_list = [k for k, v in d1.items() if v[0].startswith('array')]
print(array_fields_list)
print(statistics.median([4, 2, 3.2]))
