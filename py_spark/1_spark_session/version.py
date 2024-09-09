from  pyspark.sql.session import SparkSession
spark = SparkSession.builder.getOrCreate()
print(spark.version)
# 3.5.2