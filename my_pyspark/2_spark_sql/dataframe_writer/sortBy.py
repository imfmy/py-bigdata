from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
data = [("王五", 15), ("张三", 13), ("李四", 14), ("麻子", 16), ("tom", 1)]
df = spark.createDataFrame(data=data, schema=["name", "age"])
df.show()
# +----+---+
# |name|age|
# +----+---+
# |王五| 15|
# |张三| 13|
# |李四| 14|
# |麻子| 16|
# | tom|  1|
# +----+---+
df.coalesce(1).write.save(path='output', mode='overwrite', format='json')
# cat output/part-00000-64a41fd3-5d9e-4e2d-929b-c9d3430271b9-c000.json
# {"name":"王五","age":15}
# {"name":"张三","age":13}
# {"name":"李四","age":14}
# {"name":"麻子","age":16}
# {"name":"tom","age":1}

# sortBy与bucketBy不支持save
# 使用sortBy保证文件内是有序的，必须与分桶配合，否则报错
df.coalesce(1).write.sortBy("age").mode(saveMode='overwrite').format("json").saveAsTable("tbl_b")
# pyspark.sql.utils.AnalysisException: sortBy must be used together with bucketBy

df.coalesce(1).write.bucketBy(1, "age").sortBy("age").save(path='output', mode='overwrite', format='parquet')
# pyspark.sql.utils.AnalysisException: 'save' does not support bucketBy and sortBy right now

df.coalesce(1).write.format(source='parquet').mode(saveMode='overwrite').saveAsTable("tbl_b")
spark.read.table("tbl_b").show()
# +----+---+
# |name|age|
# +----+---+
# |王五| 15|
# |张三| 13|
# |李四| 14|
# |麻子| 16|
# | tom|  1|
# +----+---+
df.coalesce(1).write.format(source='parquet').mode(saveMode='overwrite').bucketBy(1, "age").sortBy("age").saveAsTable(
    "tbl_b")
spark.read.table("tbl_b").show()
# +----+---+
# |name|age|
# +----+---+
# | tom|  1|
# |张三| 13|
# |李四| 14|
# |王五| 15|
# |麻子| 16|
# +----+---+

####### 关闭 SparkContext #######
sc.stop()
