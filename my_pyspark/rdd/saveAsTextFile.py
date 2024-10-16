from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######


# 创建一个包含整数的 RDD
rdd = sc.parallelize([1, 2, 3, 4, 5],2)
rdd.glom().collect()
# [[1, 2], [3, 4, 5]]
# 将 RDD 保存为文本文件
rdd.saveAsTextFile("output/text_output")
# ll ./output/text_output/
# 总用量 8
# -rw-r--r--. 1 atguigu atguigu 4 10月 16 15:35 part-00000
# -rw-r--r--. 1 atguigu atguigu 6 10月 16 15:35 part-00001
# -rw-r--r--. 1 atguigu atguigu 0 10月 16 15:35 _SUCCESS

# cat output/text_output/part-00001
# 3
# 4
# 5

####### 关闭 SparkContext #######
sc.stop()
