from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
from pyspark.sql.types import *
# 定义 schema，包含一个 BooleanType 字段
schema = StructType([
    StructField("is_active", BooleanType(), nullable=True)
])

# 创建包含布尔值的 DataFrame
data = [(True,), (False,), (None,)]
df = spark.createDataFrame(data, schema)
df.printSchema()
# root
#  |-- is_active: boolean (nullable = true)
# 显示 DataFrame
df.show()
# +---------+
# |is_active|
# +---------+
# |     true|
# |    false|
# |     NULL|
# +---------+

####### 关闭 SparkContext #######
sc.stop()
