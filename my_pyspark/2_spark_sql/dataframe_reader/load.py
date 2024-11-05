from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
data = [("张三", 13), ("李四", 14), ("王五", 14)]
df = spark.createDataFrame(data=data, schema=["name", "id"])
df.show()
# +----+---+
# |name| id|
# +----+---+
# |张三| 13|
# |李四| 14|
# |王五| 14|
# +----+---+
df.write
####### 关闭 SparkContext #######
sc.stop()
