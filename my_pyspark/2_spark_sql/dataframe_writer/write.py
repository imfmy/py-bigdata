from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
data = [("张三", 13), ("李四", 14), ("王五", 14), ("麻子", 13)]
df = spark.createDataFrame(data=data, schema=["name", "age"],)
df.show()
# +----+---+
# |name|age|
# +----+---+
# |王五| 14|
# |李四| 14|
# |张三| 13|
# |麻子| 13|
# +----+---+
# 以默认参数写入csv文件
df.write.csv("csv_file/output.csv", header=True)
# ll csv_file/output.csv/
# 总用量 16
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:21 part-00000-a7a3e684-9c27-4abf-9584-9ede2bf81cdb-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:21 part-00001-a7a3e684-9c27-4abf-9584-9ede2bf81cdb-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:21 part-00002-a7a3e684-9c27-4abf-9584-9ede2bf81cdb-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:21 part-00003-a7a3e684-9c27-4abf-9584-9ede2bf81cdb-c000.csv
# -rw-r--r--. 1 atguigu atguigu  0 11月  5 10:21 _SUCCESS
# cat csv_file/output.csv/part-00001-a7a3e684-9c27-4abf-9584-9ede2bf81cdb-c000.csv
# name,id
# 李四,14

# 再次写入，会报错
df.write.csv("csv_file/output.csv", header=True)
# pyspark.sql.utils.AnalysisException: path file:/opt/module/spark-local/csv_file/output.csv already exists.

# 追加写入
df.write.csv("csv_file/output.csv",mode='append')
# ll csv_file/output.csv/
# 总用量 32
# -rw-r--r--. 1 atguigu atguigu 10 11月  5 10:25 part-00000-544817fe-cea8-451f-b117-1a13574088db-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:21 part-00000-a7a3e684-9c27-4abf-9584-9ede2bf81cdb-c000.csv
# -rw-r--r--. 1 atguigu atguigu 10 11月  5 10:25 part-00001-544817fe-cea8-451f-b117-1a13574088db-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:21 part-00001-a7a3e684-9c27-4abf-9584-9ede2bf81cdb-c000.csv
# -rw-r--r--. 1 atguigu atguigu 10 11月  5 10:25 part-00002-544817fe-cea8-451f-b117-1a13574088db-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:21 part-00002-a7a3e684-9c27-4abf-9584-9ede2bf81cdb-c000.csv
# -rw-r--r--. 1 atguigu atguigu 10 11月  5 10:25 part-00003-544817fe-cea8-451f-b117-1a13574088db-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:21 part-00003-a7a3e684-9c27-4abf-9584-9ede2bf81cdb-c000.csv
# -rw-r--r--. 1 atguigu atguigu  0 11月  5 10:25 _SUCCESS
# cat csv_file/output.csv/part-00000-544817fe-cea8-451f-b117-1a13574088db-c000.csv
# 张三,13

# 先清空文件夹再写入
df.write.csv("csv_file/output.csv",mode='overwrite')
# ll csv_file/output.csv/
# 总用量 16
# -rw-r--r--. 1 atguigu atguigu 10 11月  5 10:27 part-00000-6fe64709-7749-47e3-b1d4-a05d2fea95a3-c000.csv
# -rw-r--r--. 1 atguigu atguigu 10 11月  5 10:27 part-00001-6fe64709-7749-47e3-b1d4-a05d2fea95a3-c000.csv
# -rw-r--r--. 1 atguigu atguigu 10 11月  5 10:27 part-00002-6fe64709-7749-47e3-b1d4-a05d2fea95a3-c000.csv
# -rw-r--r--. 1 atguigu atguigu 10 11月  5 10:27 part-00003-6fe64709-7749-47e3-b1d4-a05d2fea95a3-c000.csv
# -rw-r--r--. 1 atguigu atguigu  0 11月  5 10:27 _SUCCESS
####### 关闭 SparkContext #######
sc.stop()
