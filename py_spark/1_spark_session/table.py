from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
spark.range(5).createOrReplaceTempView("table1")
spark.table("table1").sort("id").show()
# +---+
# | id|
# +---+
# |  0|
# |  1|
# |  2|
# |  3|
# |  4|
# +---+