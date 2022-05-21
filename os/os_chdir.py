# os def chdir(path: int | str | bytes | PathLike[str] | PathLike[bytes])
#   -> None
import os

current_work_directory = os.getcwd()
print(f'当前工作目录为 --> {current_work_directory}')
# 当前工作目录为 --> D:\PyCharmProjects\python-project1\os
target_directory = 'D:\\PyCharmProjects\\python-project1\\resource'
ret = os.chdir(path=target_directory)
current_work_directory = os.getcwd()
print(f'当前工作目录为 --> {current_work_directory}')
# 当前工作目录为 --> D:\PyCharmProjects\python-project1\resource
