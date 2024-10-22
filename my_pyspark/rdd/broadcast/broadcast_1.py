from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])
b.value
# [1, 2, 3, 4, 5]
spark.sparkContext.parallelize([0, 0]).flatMap(lambda x: b.value).collect()
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
b.unpersist()



####### 关闭 SparkContext #######
sc.stop()