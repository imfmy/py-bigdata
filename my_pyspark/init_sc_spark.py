from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######


####### 关闭 SparkContext #######
sc.stop()
