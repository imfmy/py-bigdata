from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
df=spark.read.json('../people.json')
# 打印schema
df.printSchema()
# root
#  |-- age: long (nullable = true)
#  |-- name: string (nullable = true)
df.show()
# +----+-------+
# | age|   name|
# +----+-------+
# |NULL|Michael|
# |  30|   Andy|
# |  19| Justin|
# +----+-------+

# 选取指定列
df.select()