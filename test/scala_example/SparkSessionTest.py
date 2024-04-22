# Scala code:
# package com.sparkbyexamples.spark
# 
# import org.apache.spark.sql.SparkSession
# 
# object SparkSessionTest {
# 
#   def main(args:Array[String]): Unit ={
# 
# 
#     val spark = SparkSession.builder()
#       .master("local[1]")
#       .appName("SparkByExample")
#       .getOrCreate();
#     
#     println("First SparkContext:")
#     println("APP Name :"+spark.sparkContext.appName);
#     println("Deploy Mode :"+spark.sparkContext.deployMode);
#     println("Master :"+spark.sparkContext.master);
# 
#     val sparkSession2 = SparkSession.builder()
#       .master("local[1]")
#       .appName("SparkByExample-test")
#       .getOrCreate();
# 
#     println("Second SparkContext:")
#     println("APP Name :"+sparkSession2.sparkContext.appName);
#     println("Deploy Mode :"+sparkSession2.sparkContext.deployMode);
#     println("Master :"+sparkSession2.sparkContext.master);
# 
#   }
# }
# 

# PySpark equivalent provided by GPT:
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder \
        .master("local[1]") \
        .appName("SparkByExample") \
        .getOrCreate()

    print("First SparkContext:")
    print("APP Name :" + spark.sparkContext.appName)
    print("Deploy Mode :" + spark.sparkContext.deployMode)
    print("Master :" + spark.sparkContext.master)

    sparkSession2 = SparkSession.builder \
        .master("local[1]") \
        .appName("SparkByExample-test") \
        .getOrCreate()

    print("Second SparkContext:")
    print("APP Name :" + sparkSession2.sparkContext.appName)
    print("Deploy Mode :" + sparkSession2.sparkContext.deployMode)
    print("Master :" + sparkSession2.sparkContext.master)