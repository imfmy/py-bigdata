from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])
b.value
# [1, 2, 3, 4, 5]

# 异步销毁
b.destroy()
# 异步销毁执行后的极短的一段时间内还是可能可以访问的
b.value
# [1, 2, 3, 4, 5]

# 销毁后的广播变量无法再次使用
b.balue
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Broadcast' object has no attribute 'balue'


b = spark.sparkContext.broadcast([1, 2, 3, 4, 5])
b.value
# [1, 2, 3, 4, 5]
b.destroy(blocking=True)
b.value

####### 关闭 SparkContext #######
sc.stop()