from pyspark import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.types import StructType

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
data = [("张三", 13), ("李四", 14), ("王五", 14), ("麻子", 13)]
df = spark.createDataFrame(data=data, schema=["name", "age"], )
df.show()
# +----+---+
# |name|age|
# +----+---+
# |王五| 14|
# |李四| 14|
# |张三| 13|
# |麻子| 13|
# +----+---+
_ = spark.sql("DROP TABLE IF EXISTS tbl_a")

df.write.saveAsTable("tbl_a")
spark.read.table("tbl_a").show()
# +----+---+
# |name| age|
# +----+---+
# |麻子| 13|
# |李四| 14|
# |王五| 14|
# |张三| 13|
# +----+---+
# 字段个数和格式必须相同，否则报错
df.selectExpr("age as col1", "name as col2").write.insertInto("tbl_a")
# pyspark.sql.utils.AnalysisException: Cannot write incompatible data to table '`default`.`tbl_a`':
# - Cannot safely cast 'age': string to bigint
df.selectExpr("name as col1", "age as col2").write.insertInto("tbl_a")
spark.read.table("tbl_a").show()
# +----+---+
# |name|age|
# +----+---+
# |麻子| 13|
# |王五| 14|
# |麻子| 13|
# |张三| 13|
# |王五| 14|
# |张三| 13|
# |李四| 14|
# |李四| 14|
# +----+---+
# 覆盖写入
df.selectExpr("name as col1", "age as col2").write.insertInto("tbl_a",overwrite=True)
spark.read.table("tbl_a").show()
# +----+---+
# |name|age|
# +----+---+
# |麻子| 13|
# |李四| 14|
# |张三| 13|
# |王五| 14|
# +----+---+
####### 关闭 SparkContext #######
sc.stop()
