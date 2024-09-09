from pyspark.sql.session import SparkSession
spark = SparkSession.builder.getOrCreate()
spark.sql("SELECT * FROM range(10) where id > 7").show()
# +---+
# | id|
# +---+
# |  8|
# |  9|
# +---+

spark.sql(
    "SELECT * FROM range(10) WHERE id > {bound1} AND id < {bound2}", bound1=7, bound2=9
).show()
# +---+
# | id|
# +---+
# |  8|
# +---+

mydf = spark.range(10)
spark.sql(
    "SELECT {col} FROM {mydf} WHERE id IN {x}",
    col=mydf.id, mydf=mydf, x=tuple(range(4))).show()
# +---+
# | id|
# +---+
# |  0|
# |  1|
# |  2|
# |  3|
# +---+

spark.sql('''
  SELECT m1.a, m2.b
  FROM {table1} m1 INNER JOIN {table2} m2
  ON m1.key = m2.key
  ORDER BY m1.a, m2.b''',
  table1=spark.createDataFrame([(1, "a"), (2, "b")], ["a", "key"]),
  table2=spark.createDataFrame([(3, "a"), (4, "b"), (5, "b")], ["b", "key"])).show()
# +---+---+
# |  a|  b|
# +---+---+
# |  1|  3|
# |  2|  4|
# |  2|  5|
# +---+---+

mydf = spark.createDataFrame([(1, 4), (2, 4), (3, 6)], ["A", "B"])
spark.sql("SELECT {df.A}, {df[B]} FROM {df}", df=mydf).show()
# +---+---+
# |  A|  B|
# +---+---+
# |  1|  4|
# |  2|  4|
# |  3|  6|
# +---+---+

spark.sql("SELECT * FROM {df} WHERE {df[B]} > :minB", {"minB" : 5}, df=mydf).show()
# +---+---+
# |  A|  B|
# +---+---+
# |  3|  6|
# +---+---+

spark.sql(
  "SELECT * FROM {df} WHERE {df[B]} > ? and ? < {df[A]}",
  args=[5, 2], df=mydf).show()
# +---+---+
# |  A|  B|
# +---+---+
# |  3|  6|
# +---+---+