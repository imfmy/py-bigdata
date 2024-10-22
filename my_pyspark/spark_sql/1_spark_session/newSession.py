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
print(spark)
spark2=spark.newSession()
print(spark2)

print("end")