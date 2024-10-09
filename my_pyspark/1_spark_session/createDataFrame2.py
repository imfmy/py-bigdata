from datetime import datetime, date
from pyspark.sql import Row
from pyspark.sql.session import  SparkSession
spark = SparkSession.builder.getOrCreate()
df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])
df.printSchema()
# root
#  |-- a: long (nullable = true)
#  |-- b: double (nullable = true)
#  |-- c: string (nullable = true)
#  |-- d: date (nullable = true)
#  |-- e: timestamp (nullable = true)
df.show()
# +---+---+-------+----------+-------------------+
# |  a|  b|      c|         d|                  e|
# +---+---+-------+----------+-------------------+
# |  1|2.0|string1|2000-01-01|2000-01-01 12:00:00|
# |  2|3.0|string2|2000-02-01|2000-01-02 12:00:00|
# |  4|5.0|string3|2000-03-01|2000-01-03 12:00:00|
# +---+---+-------+----------+-------------------+

df = spark.createDataFrame([
    (1, 2., 'string1', date(2000, 1, 1), datetime(2000, 1, 1, 12, 0)),
    (2, 3., 'string2', date(2000, 2, 1), datetime(2000, 1, 2, 12, 0)),
    (3, 4., 'string3', date(2000, 3, 1), datetime(2000, 1, 3, 12, 0))
], schema='a long, b double, c string, d date, e timestamp')
df.show()
# +---+---+-------+----------+-------------------+
# |  a|  b|      c|         d|                  e|
# +---+---+-------+----------+-------------------+
# |  1|2.0|string1|2000-01-01|2000-01-01 12:00:00|
# |  2|3.0|string2|2000-02-01|2000-01-02 12:00:00|
# |  3|4.0|string3|2000-03-01|2000-01-03 12:00:00|
# +---+---+-------+----------+-------------------+