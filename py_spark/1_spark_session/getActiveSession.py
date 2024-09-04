from pyspark.sql import SparkSession

# 检查是否存在活跃的 SparkSession
active_session = SparkSession.getActiveSession()

if not active_session:
    # 如果没有活跃的 SparkSession，则创建一个新的
    # spark = SparkSession.builder.appName("My App").getOrCreate()
    print("No active session")
else:
    # 如果存在活跃的 SparkSession，则使用它
    spark = active_session
    print(f"active session {active_session}")

# 现在可以使用 spark 来执行 Spark 操作
# spark.sql("SELECT 'Hello, World!'").show()