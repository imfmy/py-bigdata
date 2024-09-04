from pyspark.sql import SparkSession

spark = (SparkSession.builder
         .config('spark.app.name', 'app_name1')
         .getOrCreate())
spark.sparkContext.setLogLevel('INFO')
print(spark.conf.get('spark.app.name'))
# app_name1
spark.conf.set('spark.app.name', 'app_name2')
print(spark.conf.get('spark.app.name'))
# app_name2