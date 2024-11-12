

from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
from pyspark.sql.types import *
from datetime import datetime


# 定义包含 DateType 的架构
schema = StructType([
    StructField("name", StringType(), nullable=True),
    StructField("birth_date", DateType(), nullable=True)
])

# 创建 DataFrame
data = [("Alice", datetime.fromisoformat('2011-11-04')), ("Bob", datetime.fromisoformat('2021-11-04'))]
df = spark.createDataFrame(data, schema=schema)

df.printSchema()
# root
#  |-- name: string (nullable = true)
#  |-- birth_date: date (nullable = true)

df.show()
# +-----+----------+
# | name|birth_date|
# +-----+----------+
# |Alice|2011-11-04|
# |  Bob|2021-11-04|
# +-----+----------+

####### 关闭 SparkContext #######
sc.stop()
