from pyspark import SparkContext
from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = SparkContext("local", "PySpark Example")
####### 初始化 spark、sc #######

import mysql.connector

# 创建一个包含用户数据的 RDD
users_rdd = sc.parallelize([("user1", "Alice", 30), ("user2", "Bob", 25), ("user3", "Cathy", 27)])
# 定义写入数据库的函数
def write_to_db(user):
    user_id, name, age = user
    try:
        # 连接到数据库
        conn = mysql.connector.connect(host="localhost", user="your_username", password="your_password",
                                       database="your_database")
        cursor = conn.cursor()
        # 插入数据
        cursor.execute("INSERT INTO users (id, name, age) VALUES (%s, %s, %s)", (user_id, name, age))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# 使用 foreach 将每个用户数据写入数据库
users_rdd.foreach(write_to_db)

####### 关闭 SparkContext #######
sc.stop()
