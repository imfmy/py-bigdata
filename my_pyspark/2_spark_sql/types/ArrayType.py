from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
from pyspark.sql.types import ArrayType, StringType, StructField, StructType

ArrayType(StringType()) == ArrayType(StringType(), True)
# True

ArrayType(StringType(), False) == ArrayType(StringType())
# False

# 定义 schema，包含一个 ArrayType 的字段
schema = StructType([
    StructField("names", ArrayType(StringType(), containsNull=False), nullable=True)
])

# 创建包含数组数据的 DataFrame
data = [(["Alice", "Bob", "Cathy"],), (["David", "Eva"],), ([],)]
df = spark.createDataFrame(data, schema)
df.printSchema()
# root
#  |-- names: array (nullable = true)
#  |    |-- element: string (containsNull = false)
df.show()
# +-------------------+
# |              names|
# +-------------------+
# |[Alice, Bob, Cathy]|
# |       [David, Eva]|
# |                 []|
# +-------------------+

####### 关闭 SparkContext #######
sc.stop()
