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
# |name| id|
# +----+---+
# |张三| 13|
# |李四| 14|
# |王五| 14|
# +----+---+

df.write.bucketBy(2, "age").saveAsTable("example_table")
spark.read.table("example_table").show()
# +----+---+
# |name|age|
# +----+---+
# |王五| 14|
# |李四| 14|
# |张三| 13|
# |麻子| 13|
# +----+---+

####### 关闭 SparkContext #######
sc.stop()
