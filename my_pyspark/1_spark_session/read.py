from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
print(spark.read)
# <pyspark.sql.readwriter.DataFrameReader object at 0x7f0135d5be80>
import tempfile
with tempfile.TemporaryDirectory() as d:
    # Write a DataFrame into a JSON file
    spark.createDataFrame(
        [{"age": 100, "name": "Hyukjin Kwon"}]
    ).write.mode("overwrite").format("json").save(d)

    # Read the JSON file as a DataFrame.
    spark.read.format('json').load(d).show()
# +---+------------+
# |age|        name|
# +---+------------+
# |100|Hyukjin Kwon|
# +---+------------+