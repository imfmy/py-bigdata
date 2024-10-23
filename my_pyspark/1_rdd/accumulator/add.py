from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######

# 创建一个累加器，初始值为0
accumulator = sc.accumulator(0)
# 定义一个简单的加法操作
def add_to_accumulator(x):
    global accumulator
    accumulator.add(x)
# 创建一个 RDD 并对每个元素应用累加操作
rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd.foreach(add_to_accumulator)
# 打印累加器的值
print(f"Accumulated value: {accumulator.value}")
# Accumulated value: 15

####### 关闭 SparkContext #######
sc.stop()