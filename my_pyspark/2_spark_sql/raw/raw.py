from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######
from pyspark.sql import Row

row = Row(name="Alice", age=11)
print(row)
# Row(name='Alice', age=11)
print(row['name'])
# Alice
print(row['age'])
# 11
print('name' in row)
# True
print('wrong_key' in row)
# False

Person = Row("name", "age")
print(Person)
# <Row('name', 'age')>
print(Person("Alice", 11))
# Row(name='Alice', age=11)
row1 = Row("Alice", 11)
row2 = Row(name="Alice", age=11)
print(row1 == row2)
# True


# 创建 Row 对象
data = [Row(name="Alice", id=1), Row(name="Bob", id=2), Row(name="Cathy", id=3)]
rows_df = spark.createDataFrame(data)

# 显示 DataFrame
rows_df.show()
# +-----+---+
# | name| id|
# +-----+---+
# |Alice|  1|
# |  Bob|  2|
# |Cathy|  3|
# +-----+---+
# 访问列
for row in rows_df.collect():
    print(f"Name: {row.name}, ID: {row.id}")
# Name: Alice, ID: 1
# Name: Bob, ID: 2
# Name: Cathy, ID: 3
# 转换为字典
row_as_dict = rows_df.first().asDict()
print(row_as_dict)
# {'name': 'Alice', 'id': 1}

#$ cat examples/src/main/resources/people.txt
# Michael, 29
# Andy, 30
# Justin, 19
lines = sc.textFile("examples/src/main/resources/people.txt")
parts = lines.map(lambda l: l.split(","))
people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))

# Infer the schema, and register the DataFrame as a table.
schemaPeople = spark.createDataFrame(people)
schemaPeople.createOrReplaceTempView("people")

# SQL can be run over DataFrames that have been registered as a table.
teenagers = spark.sql("SELECT * FROM people ")
teenagers.show()
# +-------+---+
# |   name|age|
# +-------+---+
# |Michael| 29|
# |   Andy| 30|
# | Justin| 19|
# +-------+---+


####### 关闭 SparkContext #######
sc.stop()
