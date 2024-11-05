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
df.write.parquet(path="output/parquet", mode="error")
# ls -l output/parquet/
# 总用量 4
# -rw-r--r--. 1 atguigu atguigu 791 11月  5 15:14 part-00000-1d065451-b120-4711-ac3d-62c6a09d9918-c000.snappy.parquet
# -rw-r--r--. 1 atguigu atguigu   0 11月  5 15:14 _SUCCESS

# 再次执行会报错
# pyspark.sql.utils.AnalysisException: path file:/opt/module/spark-local/output/parquet already exists.


# age分区写入orc文件
df.write.parquet(path="output/parquet", mode="overwrite", partitionBy="age")
# ls -l output/parquet/
# 总用量 8
# drwxr-xr-x. 2 atguigu atguigu 4096 11月  5 15:15 age=13
# drwxr-xr-x. 2 atguigu atguigu 4096 11月  5 15:15 age=14
# -rw-r--r--. 1 atguigu atguigu    0 11月  5 15:15 _SUCCESS

# ls -l output/parquet/age\=13/
# 总用量 4
# -rw-r--r--. 1 atguigu atguigu 476 11月  5 15:15 part-00000-203e435e-5557-4ba1-ab5b-e2104bc1a087.c000.snappy.parquet

df.write.parquet(path="output/parquet",mode="overwrite",compression='gzip')
# ls -l output/parquet/
# 总用量 4
# -rw-r--r--. 1 atguigu atguigu 831 11月  5 15:16 part-00000-f60aa364-fa58-49d0-8c0b-9483d44fceb5-c000.gz.parquet
# -rw-r--r--. 1 atguigu atguigu   0 11月  5 15:16 _SUCCESS

####### 关闭 SparkContext #######
sc.stop()
