import json

def greet_user():
    """问候用户, 并存储其名字"""
    file_name = 'username.json'
    try:
        with open(file=file_name, mode='rt') as f:
            username = json.load(fp=f)
    except FileNotFoundError:
        username = input('请输入你的名字:')
        with open(file=file_name,mode='wt') as f:
            json.dump(obj=username,fp=f)
            print(f'当你回来时我们会记得你的,{username}')
    else:
        print(f'你好呀, {username}')

greet_user()