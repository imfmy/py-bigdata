from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######

df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
df.createOrReplaceTempView("people")

spark.sql("SELECT * FROM people").show()
# +---+-----+
# |age| name|
# +---+-----+
# |  2|Alice|
# |  5|  Bob|
# +---+-----+
df2 = df.filter(df.age > 3)
df2.createOrReplaceTempView("people")
spark.sql("SELECT * FROM people").show()
# +---+----+
# |age|name|
# +---+----+
# |  5| Bob|
# +---+----+

spark.catalog.dropTempView("people")
# True

####### 关闭 SparkContext #######
sc.stop()
