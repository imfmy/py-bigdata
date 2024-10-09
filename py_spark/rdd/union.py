from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName('')
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize(range(5), 1)
rdd2 = sc.parallelize(range(3, 8, 1), 1)
rdd1.union(rdd2).collect()
# [0, 1, 2, 3, 4, 3, 4, 5, 6, 7]
rdd1.union(rdd2).glom().collect()
# [[0, 1, 2, 3, 4], [3, 4, 5, 6, 7]]
