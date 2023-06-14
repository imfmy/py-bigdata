str1 = "crl_sop_test.sop_crl_wealth_top_list"
# print(str1.split('_crl_')[1])
org_info = '保定市交通运输局'
org_ls = org_info.split(',')
for org_pid in org_ls:
    org = org_pid.split('#@#')[0]
    pid = org_pid.split('#@#')[1]
    print(org,pid)
