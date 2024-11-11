from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
from pyspark.sql.types import *
# 定义 schema，包含一个 ByteType 字段
schema = StructType([
    StructField("rating", ByteType(), nullable=True)
])

# 创建包含字节值的 DataFrame
data = [(120,), (-10,), (127,), (None,)]
df = spark.createDataFrame(data, schema)

df.printSchema()
# root
#  |-- rating: byte (nullable = true)
# 显示 DataFrame
df.show()
# +------+
# |rating|
# +------+
# |   120|
# |   -10|
# |   127|
# |  NULL|
# +------+

####### 关闭 SparkContext #######
sc.stop()
