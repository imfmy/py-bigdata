from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######

df = spark.createDataFrame([(2, "Alice"), (5, "Bob"), (None, 'Michael')], schema=["age", "name"])
# Register the DataFrame as a global temporary view
df.createGlobalTempView("people")

# Global temporary view is tied to a system preserved database `global_temp`
spark.sql("SELECT * FROM global_temp.people").show()
# +----+-------+
# | age|   name|
# +----+-------+
# |   2|  Alice|
# |   5|    Bob|
# |null|Michael|
# +----+-------+
spark.newSession().sql("SELECT * FROM global_temp.people").show()
# +----+-------+
# | age|   name|
# +----+-------+
# |   2|  Alice|
# |   5|    Bob|
# |null|Michael|
# +----+-------+
####### 关闭 SparkContext #######
sc.stop()
