from pyspark import SparkContext, Broadcast
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######

# 广播一个字典数据
broadcast_var = sc.broadcast({"A": 1, "B": 2, "C": 3})
# 访问广播变量数据
print(broadcast_var.value)

# 当广播变量不再需要时，调用 unpersist() 释放缓存
broadcast_var.unpersist()
# 如果你想确保缓存立即清除，可以设置 blocking=True
broadcast_var.unpersist(blocking=True)

####### 关闭 SparkContext #######
sc.stop()
