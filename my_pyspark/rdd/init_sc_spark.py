from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "Collect Example")
####### 初始化 spark、sc #######

####### 关闭 SparkContext #######
sc.stop()
