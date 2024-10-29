from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()
d = [{'name': 'Alice', 'age': 1}]
# 通过python的可迭代对象创建
spark.createDataFrame([('Alice', 1), ('张三', 13), ('lisi', 12)]).show()
# +-----+---+
# |   _1| _2|
# +-----+---+
# |Alice|  1|
# | 张三| 13|
# | lisi| 12|
# +-----+---+
# 通过python的可迭代对象创建，指定schema
spark.createDataFrame([('Alice', 1), ('张三', 13), ('lisi', 12)], ['name', 'age']).show()
# +-----+---+
# | name|age|
# +-----+---+
# |Alice|  1|
# | 张三| 13|
# | lisi| 12|
# +-----+---+
# 通过python对象字典列表创建
d = [{'name': 'Alice', 'age': 1}, {'name': 'zs', 'age': 13}]
spark.createDataFrame(d).show()
# +---+-----+
# |age| name|
# +---+-----+
# |  1|Alice|
# | 13|   zs|
# +---+-----+
spark.createDataFrame(d, ['name1', 'age1']).show()
# +-----+-----+
# |name1| age1|
# +-----+-----+
# |    1|Alice|
# |   13|   zs|
# +-----+-----+

from pyspark.sql.types import *

schema = StructType([StructField("name", StringType(), True),
                     StructField("age", IntegerType(), True)])
spark.createDataFrame([('Alice', 1), ("张三", 13)], schema).show()
# +-----+---+
# | name|age|
# +-----+---+
# |Alice|  1|
# | 张三| 13|
# +-----+---+

spark.createDataFrame([('Alice', 1), ("张三", 13)], "name: string, age: int").show()
# +-----+---+
# | name|age|
# +-----+---+
# |Alice|  1|
# | 张三| 13|
# +-----+---

# 创建一个元素为空的DataFrame
spark.createDataFrame([], "name: string, age: int").show()
# +----+---+
# |name|age|
# +----+---+
# +----+---+

# 从 Row 对象创建 DataFrame
from pyspark.sql import Row

Person = Row('name', 'age')
spark.createDataFrame([Person("Alice", 1), Person("张三", 13)]).show()
# +-----+---+
# | name|age|
# +-----+---+
# |Alice|  1|
# | 张三| 13|
# +-----+---+

# 从 pandas DataFrame 创建 DataFrame。
spark.createDataFrame(
    spark.createDataFrame([Person("Alice", 1), Person("张三", 13)]).toPandas()).show()  # doctest: +SKIP
# +-----+---+
# | name|age|
# +-----+---+
# |Alice|  1|
# | 张三| 13|
# +-----+---+
import pandas

spark.createDataFrame(pandas.DataFrame([[1, 2]])).collect()  # doctest: +SKIP
# +-----+---+
# | name|age|
# +-----+---+
# |Alice|  1|
# | 张三| 13|
# +-----+---+
