from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
strlen = spark.udf.register("strlen", lambda x: len(x))
spark.sql("SELECT strlen('test')").show()
# +------------+
# |strlen(test)|
# +------------+
# |           4|
# +------------+