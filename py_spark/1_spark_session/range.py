from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()
spark.range(0, 10).show()
# +---+
# | id|
# +---+
# |  0|
# |  2|
# |  4|
# |  6|
# |  8|
# +---+
spark.range(3).show()
# +---+
# | id|
# +---+
# |  0|
# |  1|
# |  2|
# +---+