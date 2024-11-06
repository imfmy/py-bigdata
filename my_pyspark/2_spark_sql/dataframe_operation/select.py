from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
# 创建 DataFrame
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
df = spark.createDataFrame(data, ["name", "id"])
df.printSchema()
# root
#  |-- name: string (nullable = true)
#  |-- id: long (nullable = true)

df.select("*").show()
# +-----+---+
# | name| id|
# +-----+---+
# |Alice|  1|
# |  Bob|  2|
# |Cathy|  3|
# +-----+---+

df.select("name", "id", "name").show()
# +-----+---+-----+
# | name| id| name|
# +-----+---+-----+
# |Alice|  1|Alice|
# |  Bob|  2|  Bob|
# |Cathy|  3|Cathy|
# +-----+---+-----+
df.select(df[0],df[1]).show()
# +-----+---+
# | name| id|
# +-----+---+
# |Alice|  1|
# |  Bob|  2|
# |Cathy|  3|
# +-----+---+
df.select(df[2]).show()
# IndexError: list index out of range
from pyspark.sql.functions import col

df.select(col("name").alias("full_name")).show()
# +---------+
# |full_name|
# +---------+
# |    Alice|
# |      Bob|
# |    Cathy|
# +---------+

df.select("name", "id", (col("id") * 10).alias("new_id")).show()
# +-----+---+------+
# | name| id|new_id|
# +-----+---+------+
# |Alice|  1|    10|
# |  Bob|  2|    20|
# |Cathy|  3|    30|
# +-----+---+------+


df = spark.read.json("examples/src/main/resources/people.json")
# Displays the content of the DataFrame to stdout
df.show()
# +----+-------+
# | age|   name|
# +----+-------+
# |null|Michael|
# |  30|   Andy|
# |  19| Justin|
# +----+-------+
df.select(df.name, df.age + 1).show()
# +-------+---------+
# |   name|(age + 1)|
# +-------+---------+
# |Michael|     null|
# |   Andy|       31|
# | Justin|       20|
# +-------+---------+

# 更推荐['col']，以防与对象的属性字段搞混
df.select(df['name'], df['age'] + 1).show()
# +-------+---------+
# |   name|(age + 1)|
# +-------+---------+
# |Michael|     null|
# |   Andy|       31|
# | Justin|       20|
# +-------+---------+

df.select(df['age'] > 21).show()
# +----------+
# |(age > 21)|
# +----------+
# |      null|
# |      true|
# |     false|
# +----------+
####### 关闭 SparkContext #######
sc.stop()
