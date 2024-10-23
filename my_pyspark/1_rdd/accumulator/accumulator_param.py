from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######

from pyspark.accumulators import AccumulatorParam


class VectorAccumulatorParam(AccumulatorParam):
    def zero(self, value):
        return [0.0] * len(value)

    def addInPlace(self, val1, val2):
        for i in range(len(val1)):
            val1[i] += val2[i]
        return val1


va = sc.accumulator([1.0, 2.0, 3.0], VectorAccumulatorParam())
print(va.value)
# [1.0, 2.0, 3.0]


def g(x):
    global va
    va += [x] * 3


rdd = sc.parallelize([1, 2, 3])
rdd.foreach(g)
print(va.value)

####### 关闭 SparkContext #######
sc.stop()
