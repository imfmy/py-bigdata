from pyspark import SparkContext, Broadcast
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
sc = SparkContext("local", "BroadcastLoadFromPathExample")

# 使用之前保存的广播变量文件路径进行加载
broadcast_data_path = "/path/to/broadcast_data.pkl"

# 从文件路径中加载广播变量数据
broadcast_var = sc.broadcast(Broadcast.load_from_path(broadcast_data_path))

# 查看加载后的广播变量
print(broadcast_var.value)  # 假设输出为: {'A': 1, 'B': 2, 'C': 3}
####### 关闭 SparkContext #######
sc.stop()
