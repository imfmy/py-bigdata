from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
df = spark.createDataFrame([(2, "Alice"), (5, "Bob"), (1, "张三"), (4, "李四")], ["age", "name"])
# df.show()
# +---+-----+
# |age| name|
# +---+-----+
# |  2|Alice|
# |  5|  Bob|
# |  1| 张三|
# |  4| 李四|
# +---+-----+
from pyspark.sql.functions import col
# 可以通过以下方式创建Column对象
print(df.name, df['name'], df[1],col('name'))
# Column<'name'> Column<'name'> Column<'name'> Column<'name'>

####### 关闭 SparkContext #######
sc.stop()
