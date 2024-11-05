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
df.write.save(path="output/")
# ls -l output/
# 总用量 4
# -rw-r--r--. 1 atguigu atguigu 791 11月  5 15:52 part-00000-db2db02e-ca6b-4643-9bdf-fa9e1a15cc40-c000.snappy.parquet
# -rw-r--r--. 1 atguigu atguigu   0 11月  5 15:52 _SUCCESS

# 再次调用会报错
df.write.save(path="output/")
# pyspark.sql.utils.AnalysisException: path file:/opt/module/spark-local/output already exists.
####### 关闭 SparkContext #######
sc.stop()
