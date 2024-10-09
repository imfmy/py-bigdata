from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName('')
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize(range(5), 1)
rdd2 = sc.parallelize(range(3, 8, 1), 1)
rdd1.intersection(rdd2).collect()
# [4, 3]
rdd1.intersection(rdd2).glom().collect()
# [[4], [3]]
