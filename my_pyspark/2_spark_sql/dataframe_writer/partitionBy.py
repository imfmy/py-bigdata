from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
data = [("张三", 13, 1), ("李四", 14, 2), ("王五", 14, 3), ("麻子", 13, 4)]
df = spark.createDataFrame(data=data, schema=["name", "age", "id"], ).coalesce(1)
df.show()
# +----+---+---+
# |name|age| id|
# +----+---+---+
# |张三| 13|  1|
# |李四| 14|  2|
# |王五| 14|  3|
# |麻子| 13|  4|
# +----+---+---+
df.write.orc(path="output/orc", mode="error")
# ls -l output/orc/
# 总用量 4
# -rw-r--r--. 1 atguigu atguigu 404 11月  5 11:41 part-00000-230f4a9e-5e64-4834-b1bb-6efe042ac8f8-c000.snappy.orc
# -rw-r--r--. 1 atguigu atguigu   0 11月  5 11:41 _SUCCESS

# age分区写入orc文件
df.write.partitionBy("age").orc(path="output/orc", mode="overwrite")
# ls -l output/orc/
# 总用量 8
# drwxr-xr-x. 2 atguigu atguigu 4096 11月  5 15:42 age=13
# drwxr-xr-x. 2 atguigu atguigu 4096 11月  5 15:42 age=14
# -rw-r--r--. 1 atguigu atguigu    0 11月  5 15:42 _SUCCESS

# ls -l output/orc/age\=13/
# 总用量 4
# -rw-r--r--. 1 atguigu atguigu 300 11月  5 15:42 part-00000-98e7a7b2-c23e-42a5-abed-383b8691743e.c000.snappy.orc
df.write.partitionBy("age", "name").orc(path="output/orc", mode="overwrite")
# ls -l output/orc/age\=13/
# 总用量 8
# drwxr-xr-x. 2 atguigu atguigu 4096 11月  5 15:45 name=麻子
# drwxr-xr-x. 2 atguigu atguigu 4096 11月  5 15:45 name=张三

# 不能使用所有的字段作为分区字段。
df.write.partitionBy("age", "name", "id").orc(path="output/orc", mode="overwrite")
# pyspark.sql.utils.AnalysisException: Cannot use all columns for partition columns


####### 关闭 SparkContext #######
sc.stop()
