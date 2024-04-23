# Scala code:
# package com.sparkbyexamples.spark
# 
# import org.apache.spark.sql.SparkSession
# 
# trait SparkSessionWrapper {
#   lazy val spark: SparkSession = {
#     SparkSession
#       .builder()
#       .master("local")
#       .appName("spark session")
#       .config("spark.sql.shuffle.partitions", "1")
#       .getOrCreate()
#   }
# }
# 

# PySpark equivalent provided by GPT:
from pyspark.sql import SparkSession

class SparkSessionWrapper:
    @property
    def spark(self):
        return SparkSession.builder \
            .master("local") \
            .appName("spark session") \
            .config("spark.sql.shuffle.partitions", "1") \
            .getOrCreate()