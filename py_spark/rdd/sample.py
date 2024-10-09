from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName('map_partitions_with_index')
sc = SparkContext(conf=conf)

rdd = sc.parallelize(range(100), 4)
rdd.sample(False, 0.1, 1).collect()
# [11, 13, 49, 61, 65]
# 再次运行时也是一样的结果
# [11, 13, 49, 61, 65]
rdd.sample(False, 0.1).collect()
# [19, 28, 34, 48, 53, 87, 94]
rdd.sample(False, 0.1).collect()
# 再次运行时结果不一样
# [1, 7, 13, 30, 34, 35, 47, 93]