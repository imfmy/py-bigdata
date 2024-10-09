from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
# spark.sparkContext.setLogLevel("INFO")
print(spark.catalog)
# 创建一个临时视图
spark.range(1).createTempView("test_view")
tables=spark.catalog.listTables()
print(tables)
#[Table(name='test_view', catalog=None, namespace=[], description=None, tableType='TEMPORARY', isTemporary=True)]
res = spark.catalog.dropTempView("test_view")
print(res)
# True
print(spark.catalog.listTables())
# []