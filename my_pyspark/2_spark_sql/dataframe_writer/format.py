from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
data = [("张三", 13), ("李四", 14), ("王五", 14), ("麻子", 13)]
df = spark.createDataFrame(data=data, schema=["name", "id"], )
df.show()
# +----+---+
# |name|age|
# +----+---+
# |王五| 14|
# |李四| 14|
# |张三| 13|
# |麻子| 13|
# +----+---+
# 以csv文件写入
df.write.format("csv").options(header="true").save("output/csv")
# ls -l output/csv/
# 总用量 16
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:37 part-00000-d792be38-44a2-48ba-b204-b63d0011943e-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:37 part-00001-d792be38-44a2-48ba-b204-b63d0011943e-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:37 part-00002-d792be38-44a2-48ba-b204-b63d0011943e-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:37 part-00003-d792be38-44a2-48ba-b204-b63d0011943e-c000.csv
# -rw-r--r--. 1 atguigu atguigu  0 11月  5 10:37 _SUCCESS
# cat output/csv/part-00000-d792be38-44a2-48ba-b204-b63d0011943e-c000.csv
# name,id
# 张三,13

# 再次写入，会报错
df.write.format("csv").options(header="true").save("output/csv")
# pyspark.sql.utils.AnalysisException: path file:/opt/module/spark-local/csv_file/output.csv already exists.

# 追加写入
df.write.format("csv").options(header="true").mode("append").save("output/csv")
#  ls -l output/csv/
# 总用量 32
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:39 part-00000-bfe647c6-a86d-47bd-86df-6a36f9d19933-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:37 part-00000-d792be38-44a2-48ba-b204-b63d0011943e-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:39 part-00001-bfe647c6-a86d-47bd-86df-6a36f9d19933-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:37 part-00001-d792be38-44a2-48ba-b204-b63d0011943e-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:39 part-00002-bfe647c6-a86d-47bd-86df-6a36f9d19933-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:37 part-00002-d792be38-44a2-48ba-b204-b63d0011943e-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:39 part-00003-bfe647c6-a86d-47bd-86df-6a36f9d19933-c000.csv
# -rw-r--r--. 1 atguigu atguigu 18 11月  5 10:37 part-00003-d792be38-44a2-48ba-b204-b63d0011943e-c000.csv
# -rw-r--r--. 1 atguigu atguigu  0 11月  5 10:39 _SUCCESS

# 先清空文件夹再写入
df.write.format("csv").options(header="false").mode("overwrite").save("output/csv")
# ls -l output/csv/
# 总用量 16
# -rw-r--r--. 1 atguigu atguigu 10 11月  5 10:39 part-00000-62eb24d8-ec4e-4378-82e9-2493aa88784a-c000.csv
# -rw-r--r--. 1 atguigu atguigu 10 11月  5 10:39 part-00001-62eb24d8-ec4e-4378-82e9-2493aa88784a-c000.csv
# -rw-r--r--. 1 atguigu atguigu 10 11月  5 10:39 part-00002-62eb24d8-ec4e-4378-82e9-2493aa88784a-c000.csv
# -rw-r--r--. 1 atguigu atguigu 10 11月  5 10:39 part-00003-62eb24d8-ec4e-4378-82e9-2493aa88784a-c000.csv
# -rw-r--r--. 1 atguigu atguigu  0 11月  5 10:39 _SUCCESS
# cat output/csv/part-00000-62eb24d8-ec4e-4378-82e9-2493aa88784a-c000.csv
# 张三,13
####### 关闭 SparkContext #######
sc.stop()
