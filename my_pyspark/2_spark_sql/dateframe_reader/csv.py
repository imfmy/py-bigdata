from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
# sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######

import tempfile

with tempfile.TemporaryDirectory() as d:
    # Write a DataFrame into a CSV file
    df = spark.createDataFrame([{"age": 100, "name": "Hyukjin Kwon"}])
    df.write.mode("overwrite").format("csv").save(d)
    spark.read.csv(d, schema=df.schema, nullValue="Hyukjin Kwon").show()
# +---+----+
# |age|name|
# +---+----+
# |100|null|
# +---+----+

####### 关闭 SparkContext #######
# sc.stop()
