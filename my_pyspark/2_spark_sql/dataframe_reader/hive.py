from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.appName("Example").config("k1", "v1").getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######

# spark is an existing SparkSession
spark.sql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING) USING hive")
spark.sql("LOAD DATA LOCAL INPATH 'examples/src/main/resources/kv1.txt' INTO TABLE src")

# +---+-------+
# |key|  value|
# +---+-------+
# |238|val_238|
# | 86| val_86|
# |311|val_311|
# | 27| val_27|
# |165|val_165|
# |409|val_409|
# |255|val_255|
# |278|val_278|
# | 98| val_98|
# |484|val_484|
# |265|val_265|
# |193|val_193|
# |401|val_401|
# |150|val_150|
# |273|val_273|
# |224|val_224|
# |369|val_369|
# | 66| val_66|
# |128|val_128|
# |213|val_213|
# +---+-------+

# ls -l metastore_db/
# 总用量 28
# -rw-rw-r--. 1 atguigu atguigu    4 11月  7 11:17 dbex.lck
# -rw-rw-r--. 1 atguigu atguigu   38 11月  7 11:17 db.lck
# drwxrwxr-x. 2 atguigu atguigu 4096 11月  7 11:17 log
# -rw-rw-r--. 1 atguigu atguigu  608 11月  7 11:17 README_DO_NOT_TOUCH_FILES.txt
# drwxrwxr-x. 2 atguigu atguigu 4096 11月  7 11:17 seg0
# -rw-rw-r--. 1 atguigu atguigu  915 11月  7 11:17 service.properties
# drwxrwxr-x. 2 atguigu atguigu 4096 11月  7 11:17 tmp

####### 关闭 SparkContext #######
sc.stop()
