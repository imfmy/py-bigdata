from pyspark import SparkConf
from pyspark.sql import SparkSession


print("创建SparkSession对象：SparkDataFrame_001")
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
print(f"创建 DataFrameReader 对象")
dfr = spark.read
print(f"通过读取people.json文件创建DataFrame")
# {"name":"Michael"}
# {"name":"Andy", "age":30}
# {"name":"Justin", "age":19}
df = dfr.json("people.json")
# 打印 DataFrame
df.show()
# +----+-------+
# | age|   name|
# +----+-------+
# |NULL|Michael|
# |  30|   Andy|
# |  19| Justin|
# +----+-------+
