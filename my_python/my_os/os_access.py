# os
# def access(path: int | str | bytes | PathLike[str] | PathLike[bytes],
#            mode: int,
#            *,
#            dir_fd: int | None = ...,
#            effective_ids: bool = ...,
#            follow_symlinks: bool = ...) -> bool
import os
file_path = '../../resource/a.txt'
ret = os.access(path=file_path, mode=os.F_OK)
print(f'os.F_OK --> {ret}')
# os.F_OK --> True
ret = os.access(path=file_path, mode=os.R_OK)
print(f'os.R_OK --> {ret}')
# os.R_OK --> True
ret = os.access(path=file_path, mode=os.W_OK)
print(f'os.W_OK --> {ret}')
# os.W_OK --> True
ret = os.access(path=file_path, mode=os.X_OK)
print(f'os.X_OK --> {ret}')
# os.X_OK --> True