# Scala code:
# # Scala code:
# # # Scala code:
# # # # Scala code:
# # # # # Scala code:
# # # 
# # # # PySpark equivalent provided by GPT:
# # # from pyspark.sql import SparkSession
# # # 
# # # spark = SparkSession.builder.getOrCreate()
# # # sc = spark.sparkContext
# # # 
# # # data = [1, 2, 3, 4, 5]
# # # rdd = sc.parallelize(data)
# # # filteredRDD = rdd.filter(lambda x: x % 2 == 0)
# # # filteredRDD.collect()
# # 
# # # PySpark equivalent provided by GPT:
# # from pyspark.sql import SparkSession
# # 
# # spark = SparkSession.builder.getOrCreate()
# # sc = spark.sparkContext
# # 
# # data = [1, 2, 3, 4, 5]
# # rdd = sc.parallelize(data)
# # filteredRDD = rdd.filter(lambda x: x % 2 == 0)
# # filteredRDD.collect()
# 
# # PySpark equivalent provided by GPT:
# from pyspark.sql import SparkSession
# 
# spark = SparkSession.builder.getOrCreate()
# sc = spark.sparkContext
# 
# data = [1, 2, 3, 4, 5]
# rdd = sc.parallelize(data)
# filteredRDD = rdd.filter(lambda x: x % 2 == 0)
# filteredRDD.collect()

# PySpark equivalent provided by GPT:
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)
filteredRDD = rdd.filter(lambda x: x % 2 == 0)
filteredRDD.collect()