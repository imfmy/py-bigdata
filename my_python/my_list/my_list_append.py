from typing import Union, List

my_list: List[Union[None, int, str]] = []
print(my_list)
# []
my_list.append(None)
print(my_list)
# [None]
my_list.append(1)
print(my_list)
# [None, 1]
my_list.append('a')
print(my_list)
# [None, 1, 'a']
