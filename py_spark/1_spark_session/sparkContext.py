from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()

print(spark.sparkContext)
# <SparkContext master=... appName=...>
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
rdd.collect()
# [1, 2, 3, 4, 5]
