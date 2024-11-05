from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
data = [("张三", 13), ("李四", 14), ("王五", 14), ("麻子", 13)]
df = spark.createDataFrame(data=data, schema=["name", "age"])
df.show()
# +----+---+
# |name|age|
# +----+---+
# |王五| 14|
# |李四| 14|
# |张三| 13|
# |麻子| 13|
# +----+---+

df.write.text(path="output")
# pyspark.sql.utils.AnalysisException: Text data source does not support bigint data type.

####### 关闭 SparkContext #######
sc.stop()
