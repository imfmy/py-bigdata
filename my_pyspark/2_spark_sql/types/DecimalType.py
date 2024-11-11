

from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
from pyspark.sql.types import *
import decimal

# 定义包含 DecimalType 的架构
schema = StructType([
    StructField("id", IntegerType(), nullable=False),
    StructField("amount", DecimalType(precision=10, scale=2), nullable=False)
])

# 创建 DataFrame
data = [(1, decimal.Decimal('1234.56')), (2, decimal.Decimal('7890.12'))]
df = spark.createDataFrame(data, schema=schema)

df.printSchema()
# root
#  |-- id: integer (nullable = false)
#  |-- amount: decimal(10,2) (nullable = false)

df.show()
# +---+-------+
# | id| amount|
# +---+-------+
# |  1|1234.56|
# |  2|7890.12|
# +---+-------+

####### 关闭 SparkContext #######
sc.stop()
