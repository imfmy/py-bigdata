from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
path = "examples/src/main/resources/people.txt"
df1 = spark.read.text(path)
df1.show()
# +-----------+
# |      value|
# +-----------+
# |Michael, 29|
# |   Andy, 30|
# | Justin, 19|
# +-----------+
df2 = spark.read.text(path, lineSep=",")
df2.show()
# +-----------+
# |      value|
# +-----------+
# |    Michael|
# |   29\nAndy|
# | 30\nJustin|
# |       19\n|
# +-----------+
df3 = spark.read.text(path, wholetext=True)
df3.show()
# +--------------------+
# |               value|
# +--------------------+
# |Michael, 29\nAndy...|
# +--------------------+

####### 关闭 SparkContext #######
sc.stop()
