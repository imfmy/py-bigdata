# json def dump(obj: Any,
#          fp: IO[str],
#          *,
#          skipkeys: bool = ...,
#          ensure_ascii: bool = ...,
#          check_circular: bool = ...,
#          allow_nan: bool = ...,
#          cls: Type[JSONEncoder] | None = ...,
#          indent: None | int | str = ...,
#          separators: tuple[str, str] | None = ...,
#          default: (Any) -> Any | None = ...,
#          sort_keys: bool = ...,
#          **kwds: Any) -> None
import json

numbers = [2, 3, 4, 5, 6]
num1 = list(range(2, 7, 1))
file_name = 'number.json'
with open(file=file_name, mode='w') as f:
    json.dump(obj=num1, fp=f)
# 当前目录下出现文件: number.json
# [2, 3, 4, 5, 6]
