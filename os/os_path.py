import os.path

ret = os.path.abspath(__file__)
print(ret)
# D:\PyCharmProjects\python-project1\os\os_path.py
file_path = '../resource/a.txt'
# posixpath @overload def abspath(path: AnyStr) -> AnyStr
print(f'os.path.abspath -- {os.path.abspath(file_path)}')
# os.path.abspath -- D:\PyCharmProjects\python-project1\resource\a.txt
# posixpath @overload def basename(p: AnyStr) -> AnyStr
file_name = os.path.basename(file_path)
print(f'file_name -- {file_name}')
# file_name -- a.txt
print(os.path.basename('a.sss'))
# a.sss
print(f'os.path.exist(file_name) -- {os.path.exists(file_path)}')
# os.path.exist -- True
print(f'os.path.exist(a.sss) -- {os.path.exists("a.sss")}')
# os.path.exist(a.sss) -- False
