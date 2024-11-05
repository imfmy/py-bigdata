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
# 以默认参数写入json文件
df.write.json("output/json")
# ls -l output/json/
# 总用量 4
# -rw-r--r--. 1 atguigu atguigu 108 11月  5 11:11 part-00000-65a4ede3-fdc4-4e5e-b796-001a209d9514-c000.json
# -rw-r--r--. 1 atguigu atguigu   0 11月  5 11:11 _SUCCESS
# cat output/json/part-00000-65a4ede3-fdc4-4e5e-b796-001a209d9514-c000.json
# {"name":"张三","age":13}
# {"name":"李四","age":14}
# {"name":"王五","age":14}
# {"name":"麻子","age":13}

# error再次写入会报错
df.write.json("output/json")
# pyspark.sql.utils.AnalysisException: path file:/opt/module/spark-local/output/json already exists.
# 追加写入
df.write.json("output/json", mode='append')
#  ls -l output/json/
# 总用量 8
# -rw-r--r--. 1 atguigu atguigu 108 11月  5 11:11 part-00000-65a4ede3-fdc4-4e5e-b796-001a209d9514-c000.json
# -rw-r--r--. 1 atguigu atguigu 108 11月  5 11:13 part-00000-8463dc1e-db55-49ea-bb93-c177fb2cd38a-c000.json
# -rw-r--r--. 1 atguigu atguigu   0 11月  5 11:13 _SUCCESS

# 先清空文件夹再写入，并压缩文件
df.write.json("output/json", mode='overwrite',compression='gzip2')
# pyspark.sql.utils.IllegalArgumentException: Codec [gzip2] is not available. Known codecs are bzip2, deflate, uncompressed, lz4, gzip, snappy, none.
df.write.json("output/json", mode='overwrite',compression='gzip')
# ls -l output/json/
# 总用量 4
# -rw-r--r--. 1 atguigu atguigu 78 11月  5 11:15 part-00000-f88fd886-4230-4846-87f2-d7ba7449739f-c000.json.gz
# -rw-r--r--. 1 atguigu atguigu  0 11月  5 11:15 _SUCCESS
####### 关闭 SparkContext #######
sc.stop()
