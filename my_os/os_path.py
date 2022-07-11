import os.path
import sys

print(sys.path)
print(__file__, 'xxx')
ret = os.path.abspath(__file__)
print(ret)
# D:\PyCharmProjects\python-project1\os\os_path.py

# 获取文件的绝对路径
file_path = '../resource/a.txt'
print(f'{os.path.abspath(file_path)}')
# D:\PyCharmProjects\python-project1\resource\a.txt

# 获取文件的目录名：
print(os.path.dirname(file_path))

# os.path.basename() 获取文件名
file_name = os.path.basename(file_path)
print(f'{file_name}')
# a.txt
print(os.path.basename('a.sss'))
# a.sss

# 获取文件绝对路径目录的父目录
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# D:\Projects\pythonProject

# 判断文件是否存在
print(f'os.path.exist(file_name) -- {os.path.exists(file_path)}')
# os.path.exist -- True
print(f'os.path.exist(a.sss) -- {os.path.exists("a.sss")}')
# os.path.exist(a.sss) -- False
