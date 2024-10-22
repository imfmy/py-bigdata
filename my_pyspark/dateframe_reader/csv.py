from pyspark.sql import SparkSession

# 创建 SparkSession
spark = SparkSession.builder.appName("CSVReaderExample").getOrCreate()

# 读取 CSV 文件
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True, sep=",")

# 展示前 5 行
df.show(5)

# 停止 SparkSession
spark.stop()
