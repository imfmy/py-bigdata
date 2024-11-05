import os.path
from pyspark.sql.session import SparkSession

path = 'people.csv'
path1 = ['people.csv', 'people1.csv']
# print(os.path.exists(path))
spark = SparkSession.builder.getOrCreate()
df = spark.read.csv(path1)
df.show()
# +------------------+
# |      name;age;job|
# |Jorge;30;Developer|
# |  Bob;32;Developer|
# |      name;age;job|
# |Jorge;30;Developer|
# |  Bob;32;Developer|
# +------------------+
df2 = spark.read.option("delimiter", ";").option("header", True).csv(path1)
# df2 = spark.read.options(delimiter=";", header=True).csv(path1)
df2.show()
# +-----+---+---------+
# | name|age|      job|
# +-----+---+---------+
# |Jorge| 30|Developer|
# |  Bob| 32|Developer|
# |Jorge| 30|Developer|
# |  Bob| 32|Developer|
# +-----+---+---------+

