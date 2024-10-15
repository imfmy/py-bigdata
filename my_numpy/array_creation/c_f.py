import numpy as np
import time

# 创建一个大数组
size = 10000
a_c = np.random.rand(size, size)  # 默认 C-order
a_f = np.asfortranarray(a_c)      # 转换为 F-order

# 按行遍历 C-order 数组
start = time.time()
for i in range(size):
    for j in range(size):
        _ = a_c[i, j]
end = time.time()
print(f"按行遍历 C-order 数组: {end - start:.4f} 秒")
# 按行遍历 C-order 数组: 7.2242 秒

# 按列遍历 C-order 数组
start = time.time()
for j in range(size):
    for i in range(size):
        _ = a_c[i, j]
end = time.time()
print(f"按列遍历 C-order 数组: {end - start:.4f} 秒")
# 按列遍历 C-order 数组: 10.1202 秒

# 按行遍历 F-order 数组
start = time.time()
for i in range(size):
    for j in range(size):
        _ = a_f[i, j]
end = time.time()
print(f"按行遍历 F-order 数组: {end - start:.4f} 秒")
# 按行遍历 F-order 数组: 9.7708 秒

# 按列遍历 F-order 数组
start = time.time()
for j in range(size):
    for i in range(size):
        _ = a_f[i, j]
end = time.time()
print(f"按列遍历 F-order 数组: {end - start:.4f} 秒")
# 按列遍历 F-order 数组: 7.3326 秒
