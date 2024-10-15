import numpy as np

# 创建一个原型数组
prototype = np.array([[1, 2, 3], [4, 5, 6]])

# 使用 empty_like 创建未初始化的数组
empty_array = np.empty_like(prototype)

print("原型数组:\n", prototype)
# 原型数组:
#  [[1 2 3]
#  [4 5 6]]
print("未初始化的数组:\n", empty_array)
# 未初始化的数组:
#  [[2220012842576 2220490210272 2220489865536]
#  [2220490211600 2220012843376 2220012842704]]


# 创建一个原型数组
prototype = np.array([1.5, 2.5, 3.5])

# 使用 empty_like 创建整数类型的未初始化数组
empty_int_array = np.empty_like(prototype, dtype=int)

print("原型数组:\n", prototype)
# 原型数组:
#  [1.5 2.5 3.5]
print("整数类型的未初始化数组:\n", empty_int_array)
# 整数类型的未初始化数组:
#  [4607182418800017408 4607182418800017408 4607182418800017408]


# 指定内存布局顺序
# 创建一个 Fortran-style 的原型数组
prototype = np.array([[1, 2, 3], [4, 5, 6]], order='F')

# 使用 empty_like 创建 Fortran-style 的未初始化数组
empty_fortran_array = np.empty_like(prototype, order='F')

print("原型数组的内存布局:\n", prototype)
# 原型数组的内存布局:
#  [[1 2 3]
#  [4 5 6]]
print("Fortran-style 的未初始化数组:\n", empty_fortran_array)
# Fortran-style 的未初始化数组:
#  [[8223637208517730856 8007464404762783586        500068589630]
#  [7070700224581493605 3251644510822034018       3052880289840]]