from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
from pyspark.sql import Row

# spark is from the previous example.
# Create a simple DataFrame, stored into a partition directory
sc = spark.sparkContext

squaresDF = spark.createDataFrame(sc.parallelize(range(1, 6))
                                  .map(lambda i: Row(single=i, double=i ** 2)))
squaresDF.show()
# +------+------+
# |single|double|
# +------+------+
# |     1|     1|
# |     2|     4|
# |     3|     9|
# |     4|    16|
# |     5|    25|
# +------+------+

squaresDF.write.parquet("data/test_table/key=1")

# Create another DataFrame in a new partition directory,
# adding a new column and dropping an existing column
cubesDF = spark.createDataFrame(sc.parallelize(range(6, 11))
                                .map(lambda i: Row(single=i, triple=i ** 3)))
cubesDF.show()
# +------+------+
# |single|triple|
# +------+------+
# |     6|   216|
# |     7|   343|
# |     8|   512|
# |     9|   729|
# |    10|  1000|
# +------+------+

cubesDF.write.parquet("data/test_table/key=2")

# Read the partitioned table
mergedDF = spark.read.option("mergeSchema", "true").parquet("data/test_table")
mergedDF.printSchema()

# The final schema consists of all 3 columns in the Parquet files together
# with the partitioning column appeared in the partition directory paths.
# root
#  |-- double: long (nullable = true)
#  |-- single: long (nullable = true)
#  |-- triple: long (nullable = true)
#  |-- key: integer (nullable = true)

mergedDF.show()
# +------+------+------+---+
# |single|double|triple|key|
# +------+------+------+---+
# |     4|    16|  NULL|  1|
# |     5|    25|  NULL|  1|
# |     9|  NULL|   729|  2|
# |    10|  NULL|  1000|  2|
# |     2|     4|  NULL|  1|
# |     3|     9|  NULL|  1|
# |     1|     1|  NULL|  1|
# |     6|  NULL|   216|  2|
# |     7|  NULL|   343|  2|
# |     8|  NULL|   512|  2|
# +------+------+------+---+


####### 关闭 SparkContext #######
sc.stop()
