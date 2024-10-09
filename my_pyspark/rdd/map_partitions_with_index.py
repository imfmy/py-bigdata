from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName('map_partitions_with_index')
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5], 3)
def f(splitIndex, iterator):
    for i in iterator:
        yield (splitIndex, i)


rdd.mapPartitionsWithIndex(f).collect()
# [(0, 1), (1, 2), (1, 3), (2, 4), (2, 5)]
rdd.mapPartitionsWithIndex(f).glom().collect()