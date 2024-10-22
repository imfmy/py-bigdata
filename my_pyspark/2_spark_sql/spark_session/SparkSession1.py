from pyspark import SparkConf
from pyspark.sql import SparkSession
print("创建SparkSession对象：SparkSession_001")
spark = (SparkSession.builder
         .master("local[*]")
         .appName("SparkSession_001")
         .config("spark.some.config.option", "some-value")
         .config(conf=SparkConf())
         .config(map={"spark.some.config.number": 123, "spark.some.config.float": 0.123})
         .getOrCreate())

print(f"当前Spark版本：{spark.version}")
sc = spark.sparkContext
# 设置日志级别为INFO
sc.setLogLevel("INFO")
print("end")
# 创建SparkSession对象：SparkSession_001
# Setting default log level to "WARN".
# To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
# 当前Spark版本：3.5.2
# 24/09/04 11:11:34 INFO SparkContext: Invoking stop() from shutdown hook
# 24/09/04 11:11:34 INFO SparkContext: SparkContext is stopping with exitCode 0.