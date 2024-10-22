from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######

# 创建一个包含键值对的 RDD
rdd = sc.parallelize([("apple", 3), ("banana", 2), ("cherry", 5), ("date", 7), ], 2)
# 将 RDD 保存为 SequenceFile
rdd.saveAsSequenceFile("output/sequence_output")
# ls -l output/sequence_output/
# 总用量 8
# -rw-r--r--. 1 atguigu atguigu 122 10月 16 15:58 part-00000
# -rw-r--r--. 1 atguigu atguigu 121 10月 16 15:58 part-00001
# -rw-r--r--. 1 atguigu atguigu   0 10月 16 15:58 _SUCCESS

####### 关闭 SparkContext #######
sc.stop()
