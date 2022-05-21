# os def chmod(path: int | str | bytes | PathLike[str] | PathLike[bytes],
#           mode: int,
#           *,
#           dir_fd: int | None = ...,
#           follow_symlinks: bool = ...) -> None
import os, stat

file_path = '../resource/a.txt'
os.chmod(path=file_path, mode=stat.S_IXUSR)
