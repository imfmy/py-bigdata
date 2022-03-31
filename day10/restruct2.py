import json


def get_stored_username():
    """如果存储了用户名，就返回用户名"""
    filename = 'username.json'
    try:
        with open(file=filename) as f:
            username = json.load(fp=f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    "提示用户输入名称，然后存储"
    username = input("请输入你的姓名：")
    filename = 'username.json'
    with open(file=filename, mode='w') as f:
        json.dump(obj=username, fp=f)
    return username


def greet_user():
    """问候客户，并指出其名字"""
    username = get_stored_username()
    if username:
        print(f'你好啊，{username}')
    else:
        username=get_new_username()
        print(f'我会记的你的，{username}')
get_new_username()
# Jack
greet_user()
# 你好啊，Jack