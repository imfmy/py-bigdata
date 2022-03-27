# builtins
# @overload
# def open(file: str | bytes | PathLike[str] | PathLike[bytes] | int,
#          mode: str,
#          buffering: int = ...,
#          encoding: str | None = ...,
#          errors: str | None = ...,
#          newline: str | None = ...,
#          closefd: bool = ...,
#          opener: (str, int) -> int | None = ...) -> IO

# typing.IO @abstractmethod def read(self, n: int = ...) -> AnySt
with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(file_object)
# <_io.TextIOWrapper name='pi_digits.txt' mode='r' encoding='cp936'>
print(type(contents))
# <class 'str'>
print(contents.rstrip())
# 3.1415926535
#   8979323846
#   2643383279
