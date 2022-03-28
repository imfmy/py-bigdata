# typing.IO @abstractmethod def readlines(self, hint: int = ...) -> list[AnyStr]
file_name = 'pi_digits.txt'
with open(file_name, encoding='utf-8') as io_object:
    lines = io_object.readlines()
print(type(lines))
# <class 'list'>
print(lines)
# ['你3.1415926535\n', '  8979323846\n', '  2643383279']
for e in lines:
    print(e.rstrip())
# 你3.1415926535
#   8979323846
#   2643383279