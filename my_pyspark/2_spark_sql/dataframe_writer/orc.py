from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
data = [("张三", 13), ("李四", 14), ("王五", 14), ("麻子", 13)]
df = spark.createDataFrame(data=data, schema=["name", "age"], ).coalesce(1)
df.show()
# +----+---+
# |name|age|
# +----+---+
# |王五| 14|
# |李四| 14|
# |张三| 13|
# |麻子| 13|
# +----+---+
df.write.orc(path="output/orc", mode="error")
# ls -l output/orc/
# 总用量 4
# -rw-r--r--. 1 atguigu atguigu 404 11月  5 11:41 part-00000-230f4a9e-5e64-4834-b1bb-6efe042ac8f8-c000.snappy.orc
# -rw-r--r--. 1 atguigu atguigu   0 11月  5 11:41 _SUCCESS

# age分区写入orc文件
df.write.orc(path="output/orc", mode="overwrite", partitionBy="age")
# ls -l output/orc/
# 总用量 8
# drwxr-xr-x. 2 atguigu atguigu 4096 11月  5 11:40 age=13
# drwxr-xr-x. 2 atguigu atguigu 4096 11月  5 11:40 age=14
# -rw-r--r--. 1 atguigu atguigu    0 11月  5 11:40 _SUCCESS
####### 关闭 SparkContext #######
sc.stop()
