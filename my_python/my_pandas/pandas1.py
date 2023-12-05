import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    8.0
# dtype: float64

dates = pd.date_range("20130101", periods=6)
print(dates)
# DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
#                '2013-01-05', '2013-01-06'],
#               dtype='datetime64[ns]', freq='D')


data1 = np.random.randn(6, 4)
print(f'data1_type:{type(dates)}')
print(f'data1:{data1}')

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
#                    A         B         C         D
# 2013-01-01 -0.959188  0.792970  0.234534  0.745526
# 2013-01-02 -0.064245 -0.326922  0.784081  2.707713
# 2013-01-03  0.670060  0.213183  2.016578 -2.670497
# 2013-01-04  0.081221 -0.608579  1.063223  1.687331
# 2013-01-05 -0.568081  0.850861 -0.353981 -0.519961
# 2013-01-06 -0.261178 -0.296354  1.443860 -1.224802


# 创建一个2行2列的DataFrame（二维表）
df2 = pd.DataFrame(data=[[1, 2], [3, 4]], index=['l1', 'l2'], columns=['c1', 'c2'])
print(df2)
#     c1  c2
# l1   1   2
# l2   3   4
# 查看类型
print(df2.dtypes)
# c1    int64
# c2    int64
# dtype: object

# 通过字典创建DataFrame
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print("通过字典创建DataFrame：")
print(df2)
#      A          B    C  D      E    F
# 0  1.0 2013-01-02  1.0  3   test  foo
# 1  1.0 2013-01-02  1.0  3  train  foo
# 2  1.0 2013-01-02  1.0  3   test  foo
# 3  1.0 2013-01-02  1.0  3  train  foo

# 查看表前n行数据，类似sql中的limit，不输入的话默认5行
h1 = df2.head(2)
print("查看前2行：")
print(h1)
#      A          B    C  D      E    F
# 0  1.0 2013-01-02  1.0  3   test  foo
# 1  1.0 2013-01-02  1.0  3  train  foo

# 查看表后n行数据，
t1 = df2.tail(3)
print("======查看后3行数据=====：")
print(t1)
#      A          B    C  D      E    F
# 1  1.0 2013-01-02  1.0  3  train  foo
# 2  1.0 2013-01-02  1.0  3   test  foo
# 3  1.0 2013-01-02  1.0  3  train  foo

# 查看DataFrame的index和columns
idx1 = df2.index
print("======查看DataFrame的index和columns======")
print(idx1)
# Index([0, 1, 2, 3], dtype='int64')

col1 = df2.columns
print("======查看columns======")
print(col1)
# Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')


np1 = df2.to_numpy()
print("=====将dataframe的数据转为numpy")
print(type(np1))
# <class 'numpy.ndarray'>
print(np1)
# [[1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
#  [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']
#  [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
#  [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']]

# dataframe数据统计摘要
dsc1 = df2.describe()
print('=====describe=====')
print(dsc1)
#          A                    B    C    D
# count  4.0                    4  4.0  4.0
# mean   1.0  2013-01-02 00:00:00  1.0  3.0
# min    1.0  2013-01-02 00:00:00  1.0  3.0
# 25%    1.0  2013-01-02 00:00:00  1.0  3.0
# 50%    1.0  2013-01-02 00:00:00  1.0  3.0
# 75%    1.0  2013-01-02 00:00:00  1.0  3.0
# max    1.0  2013-01-02 00:00:00  1.0  3.0
# std    0.0                  NaN  0.0  0.0


# 置换数据
t1 = df2.T
print('=====T=====')
print(t1)

# 创建一个2行2列的DataFrame（二维表）
df = pd.DataFrame(data=[[1, "张三", 13], [2, "李四", 14], [3, "王五", 15]], index=['l1', 'l2', 'l3'],
                  columns=['id', 'name', 'age'])
print('=====定义index=====')
print(df)
#    id name  age
# 1   1   张三   13
# 2   2   李四   14
# l3   3   王五   15

df = pd.DataFrame(data=[[1, "张三", 13], [2, "李四", 14], [3, "王五", 15]],
                  columns=['id', 'name', 'age'])
print('=====无定义index=====')
print(df)
#    id name  age
# 0   1   张三   13
# 1   2   李四   14
# 2   3   王五   15
#  获取某个字段
print('====id=====')
print(df["id"])

print('=====行（index)切片=====')
print('=====选取第2行=====')
#    id name  age
# 1   2   李四   14
print(df[1:2])
print('=====选取第1行=====')
print(df[0:1])
#    id name  age
# 0   1   张三   13

print('=====选取第1行第name列的DataFrame=====')
data2 = df.loc[0:0, ["name"]]
print(data2)
print(type(data2))

print('====获取第index行第col列的值=====')
data3 = df.at[0, "name"]
print(data3, type(data3))
# 张三 <class 'str'>
data_1_age = df.at[1, 'age']
print(data_1_age, type(data_1_age))
# 14 <class 'numpy.int64'>
