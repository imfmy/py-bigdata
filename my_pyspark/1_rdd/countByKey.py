from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######

# 创建一个包含单词的 RDD
words_rdd = sc.parallelize([("spark", 2), ("hadoop", 1), ("spark", 4), ("flink", 1), ("hadoop", 1), ("spark", 1)])
# 使用 countByKey 统计每个单词的出现次数
word_counts = words_rdd.countByKey()


# spark: 3
# hadoop: 2
# flink: 1

####### 关闭 SparkContext #######
sc.stop()
