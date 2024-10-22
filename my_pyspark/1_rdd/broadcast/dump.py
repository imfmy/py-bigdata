from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
# 创建广播变量
data = {"A": 1, "B": 2, "C": 3}
broadcast_var = sc.broadcast(data)

# 打开一个二进制文件以进行写入
with open("broadcast_data.pkl", "wb") as f:
    # 将广播数据 dump 到文件中
    broadcast_var.dump(broadcast_var.value, f)

# [atguigu@hadoop102:/opt/module/spark-local]$ ll
# -rw-rw-r--. 1 atguigu atguigu    34 10月 22 15:26 broadcast_data.pkl

import pickle
# 检查文件是否已成功写入（可以通过重新加载来验证）
with open("broadcast_data.pkl", "rb") as f:
    loaded_data = pickle.load(f)
    print(loaded_data)  # 输出: {'A': 1, 'B': 2, 'C': 3}
# {'A': 1, 'B': 2, 'C': 3}
####### 关闭 SparkContext #######
sc.stop()