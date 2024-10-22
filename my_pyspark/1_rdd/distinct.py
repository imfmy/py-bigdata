from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "Example")
####### 初始化 spark、sc #######
rdd1=sc.parallelize([1,1,2,2,2,3],3)
print(rdd1.glom().collect())
print(rdd1.distinct(2).glom().collect())
####### 关闭 SparkContext #######
sc.stop()
