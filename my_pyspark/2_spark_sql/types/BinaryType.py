from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
from pyspark.sql.types import ArrayType, StringType, StructField, StructType, BinaryType

# 定义 schema，包含一个 BinaryType 字段
schema = StructType([
    StructField("file_content", BinaryType(), nullable=False)
])

# 创建包含二进制数据的 DataFrame
data = [(b'\x01\x02\x03\x04',), (b'\x55\x06\x07\x08',)]
df = spark.createDataFrame(data, schema)
df.printSchema()
# root
#  |-- file_content: binary (nullable = false)
df.show()
# +-------------+
# | file_content|
# +-------------+
# |[01 02 03 04]|
# |[05 06 07 08]|
# +-------------+

####### 关闭 SparkContext #######
sc.stop()
