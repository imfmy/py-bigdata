import numpy as np

# 创建一个 3x3 的未初始化数组
empty_array = np.empty((2, 3))
print("未初始化数组:\n", empty_array)
# 未初始化数组:
#  [[0.   0.15 0.25]
#  [0.5  0.75 1.  ]]

# 指定数据类型
empty_int_array = np.empty((2, 3), dtype=int)
print("未初始化的整数数组:\n", empty_int_array)
# 未初始化的整数数组:
#  [[                  0 4594572339843380019 4598175219545276416]
#  [4602678819172646912 4604930618986332160 4607182418800017408]]

# 指定数组的存储顺序
# 创建一个 2x2 的未初始化数组，使用 Fortran 风格的存储顺序
empty_fortran_array = np.empty((2, 2), order='F')
print("Fortran 风格的未初始化数组:\n", empty_fortran_array)
# Fortran 风格的未初始化数组:
#  [[ 1.02380627e-306  8.77010924e-301]
#  [ 3.96786132e-301 -1.00581973e+060]]