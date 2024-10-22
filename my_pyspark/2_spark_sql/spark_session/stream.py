from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
print(spark.streams)
# <pyspark...StreamingQueryManager object ...>
sq = spark.readStream.format("rate").load().writeStream.format('memory').queryName('this_query').start()
sqm = spark.streams
[print(q.name) for q in sqm.active]
# ['this_query']
sq.stop()
