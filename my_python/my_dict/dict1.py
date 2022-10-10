import json

str1 = '{"用户评价":"8.33","物流时效":"7.32","售后服务":"9.70"}'
js1 = json.loads(str1)
print(type(js1), js1)
# <class 'dict'> {'用户评价': '8.33', '物流时效': '7.32', '售后服务': '9.70'}
print(js1.keys, js1.keys(), list(js1.keys()))
# <built-in method keys of dict object at 0x000001DDC9739580> dict_keys(['用户评价', '物流时效', '售后服务']) ['用户评价', '物流时效', '售后服务']
print(set(['用户评价','物流时效','1']) < set(js1.keys()))
