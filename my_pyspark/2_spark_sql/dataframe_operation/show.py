from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######


data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
df = spark.createDataFrame(data, ["name", "id"])
# 显示前 2 行
df.show(2)
# +-----+---+
# | name| id|
# +-----+---+
# |Alice|  1|
# |  Bob|  2|
# +-----+---+
# only showing top 2 rows

df = spark.createDataFrame([(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
df.show(truncate=3)
# +---+----+
# |age|name|
# +---+----+
# | 14| Tom|
# | 23| Ali|
# | 16| Bob|

df.show(vertical=True)
# -RECORD 0-----
#  age  | 14
#  name | Tom
# -RECORD 1-----
#  age  | 23
#  name | Alice
# -RECORD 2-----
#  age  | 16
#  name | Bob





####### 关闭 SparkContext #######
sc.stop()
