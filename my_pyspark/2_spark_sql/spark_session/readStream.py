from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
print(spark.readStream)
import time
df = spark.readStream.format("rate").load()
df = df.selectExpr("value % 3 as v")
q = df.writeStream.format("console").start()
time.sleep(3)
q.stop()