# json def load(fp: SupportsRead[str | bytes],
#          *,
#          cls: Type[JSONDecoder] | None = ...,
#          object_hook: (dict) -> Any | None = ...,
#          parse_float: (str) -> Any | None = ...,
#          parse_int: (str) -> Any | None = ...,
#          parse_constant: (str) -> Any | None = ...,
#          object_pairs_hook: (list[tuple[Any, Any]]) -> Any | None = ...,
#          **kwds: Any) -> Any
import json
file_name = 'number.json'
with open(file=file_name,mode='rt') as f:
    num = json.load(fp=f)
print(num)
# [2, 3, 4, 5, 6]
