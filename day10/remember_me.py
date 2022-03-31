import json

# 如果存储了用户名就加载它, 否则提示输入用户名并存储
file_name = 'username.json'
try:
    with open(file=file_name, mode='rt') as f:
        username = json.load(fp=f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(file=file_name, mode='wt') as f:
        json.dump(obj=username, fp=f)
        print(f'We will remember you when you comback , {username}')
else:
    print(f'Welcome back, {username}!')
# Welcome back, Fmy!
