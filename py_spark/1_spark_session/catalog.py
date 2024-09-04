from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("INFO")
# 列出所有数据库
databases = spark.catalog.listDatabases()
print(databases)
# [Database(name='default', catalog='spark_catalog', description='default database', locationUri='file:/C:/Users/imfmy/Documents/PycharmProjects/py-bigdata/py_spark/1_spark_session/spark-warehouse')]
# 列出当前数据库中的所有表
tables = spark.catalog.listTables()
print(tables)
# []