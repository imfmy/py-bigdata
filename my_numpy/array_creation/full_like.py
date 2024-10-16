import numpy as np

# 创建一个原型数组
prototype = np.array([[2, 3, 4], [5, 6, 7]])
# 使用 full_like 创建全 9 数组
full_nine = np.full_like(prototype, fill_value=9)
print("与原型数组相同形状和类型的全 9 数组:\n", full_nine)
# 与原型数组相同形状和类型的全 9 数组:
#  [[9 9 9]
#  [9 9 9]]

# 创建一个原型数组
prototype = np.array([0.5, 1.5, 2.5])
# 使用 full_like 创建整数类型的全 5 数组
full_int = np.full_like(prototype, fill_value=5, dtype=int)
print("整数类型的全 5 数组:", full_int)
# 整数类型的全 5 数组: [5 5 5]

# 使用 full_like 创建布尔类型的全 True 数组
full_bool = np.full_like(prototype, fill_value=True, dtype=bool)
print("布尔类型的全 True 数组:", full_bool)
# 布尔类型的全 True 数组: [ True  True  True]

# 创建一个原型数组
prototype = np.array([[1, 2], [3, 4]])
# 使用 full_like 创建一个形状为 (3, 3) 的全 7 数组
full_reshaped = np.full_like(prototype, fill_value=7, shape=(3, 3))
print("指定新形状的全 7 数组:\n", full_reshaped)
#  [[7 7 7]
#  [7 7 7]
#  [7 7 7]]

