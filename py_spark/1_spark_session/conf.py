from pyspark.sql import SparkSession

spark = (SparkSession.builder
         .config('spark.app.name', 'app_name1')
         .getOrCreate())
spark.sparkContext.setLogLevel('INFO')
print(spark.conf
        )
print(spark.conf.get('spark.app.name'))