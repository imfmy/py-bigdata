from pyspark import SparkContext, Broadcast
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
from pyspark import Broadcast

# 检查文件是否已成功写入（可以通过重新加载来验证）
with open("broadcast_data.pkl", "rb") as f:
    loaded_data = pickle.load(f)
    print(loaded_data)  # 输出: {'A': 1, 'B': 2, 'C': 3}
# {'A': 1, 'B': 2, 'C': 3}

loaded_data2 = sc.broadcast(1)
# 假设我们之前使用 dump() 方法保存了广播变量数据到文件 'broadcast_data.pkl'
with open("broadcast_data.pkl", "rb") as f:
    # 加载广播数据
    print(loaded_data2.load(f))
    # {'A': 1, 'B': 2, 'C': 3}
    print(loaded_data2.value)
    # 1
####### 关闭 SparkContext #######
sc.stop()
