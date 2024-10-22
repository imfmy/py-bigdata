from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
a = sc.accumulator(0)
print(a.value)
# 0

a.value = 2
print(a.value)
# 2

a += 5
print(a.value)
# 7

rdd = sc.parallelize([1, 2, 3])


def f(x):
    global a
    a += x


rdd.foreach(f)
print(a.value)
# 13

b = sc.accumulator(0)

def g(x):
    b.add(x)

rdd.foreach(g)
print(b.value)
####### 关闭 SparkContext #######
sc.stop()
