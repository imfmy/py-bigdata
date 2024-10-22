from pyspark import SparkContext, StorageLevel
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######

# 创建一个 RDD
data_rdd = sc.parallelize([1, 2, 3, 4, 5])
# 将 RDD 缓存到内存
data_rdd.cache()
# 第一次行动操作，触发计算并缓存
sum_result = data_rdd.sum()
print(f"Sum: {sum_result}")
# Sum: 15
# 第二次操作直接从内存中读取
count_result = data_rdd.count()
print(f"Count: {count_result}")
# Count: 5


rdd = sc.parallelize([1, 2, 3, 4, 5])
# 将 RDD 持久化到内存
rdd.persist(StorageLevel.MEMORY_ONLY)
# 第一次行动操作，触发 RDD 计算并持久化
result = rdd.sum()
print(f"Sum: {result}")
# Sum: 15
# 第二次操作直接从内存读取，无需重新计算
count = rdd.count()
print(f"Count: {count}")
Count: 5
####### 关闭 SparkContext #######
sc.stop()