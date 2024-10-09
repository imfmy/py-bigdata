from typing import Any


def fun(*, name: str) -> Any:
    print(name)

if __name__ == '__main__':
    fun(name="John")
