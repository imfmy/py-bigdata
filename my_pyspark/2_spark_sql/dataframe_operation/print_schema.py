from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
df = spark.createDataFrame(
    [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
df.printSchema()
# root
#  |-- age: long (nullable = true)
#  |-- name: string (nullable = true)

df = spark.createDataFrame([(1, (2,2))], ["a", "b"])
df.printSchema()
# root
#  |-- a: long (nullable = true)
#  |-- b: struct (nullable = true)
#  |    |-- _1: long (nullable = true)
#  |    |-- _2: long (nullable = true)
df.printSchema(1)
# root
#  |-- a: long (nullable = true)
#  |-- b: struct (nullable = true)
df.printSchema(2)
# root
#  |-- a: long (nullable = true)
#  |-- b: struct (nullable = true)
#  |    |-- _1: long (nullable = true)
#  |    |-- _2: long (nullable = true)



####### 关闭 SparkContext #######
sc.stop()
