import os
os.environ['PYTHONPATH']=os.environ['PYTHONPATH']+":/opt/module/spark-3.5.2-bin-hadoop3/python/lib/pyspark.zip:/opt/module/spark-3.5.2-bin-hadoop3/python/lib/py4j-0.10.9.7-src.zip"

from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()
d = [{'name': 'Alice', 'age': 1}]
spark.createDataFrame(d).show()