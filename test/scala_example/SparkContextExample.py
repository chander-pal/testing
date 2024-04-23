# Scala code:
# package com.sparkbyexamples.spark
# 
# import com.sparkbyexamples.spark.dataframe.functions.SortExample.spark
# import org.apache.spark.SparkContext
# import org.apache.spark.sql.{SQLContext, SparkSession}
# 
# object SparkContextExample extends App{
# 
#   val spark = SparkSession.builder()
#     .master("local[1]")
#     .appName("SparkByExamples.com")
#     .getOrCreate();
# 
#   spark.sparkContext.setLogLevel("ERROR")
# 
# 
#   val sparkContext:SparkContext = spark.sparkContext
#   val sqlCon:SQLContext = spark.sqlContext
# 
#   val sqlContext = new org.apache.spark.sql.SQLContext(spark.sparkContext)
# 
#   println("First SparkContext:")
#   println("APP Name :"+spark.sparkContext.appName);
#   println("Deploy Mode :"+spark.sparkContext.deployMode);
#   println("Master :"+spark.sparkContext.master);
# 
#   val sparkSession2 = SparkSession.builder()
#     .master("local[1]")
#     .appName("SparkByExample-test")
#     .getOrCreate();
# 
#   println("Second SparkContext:")
#   println("APP Name :"+sparkSession2.sparkContext.appName);
#   println("Deploy Mode :"+sparkSession2.sparkContext.deployMode);
#   println("Master :"+sparkSession2.sparkContext.master);
# 
# 
# }
# 

# PySpark equivalent provided by GPT:
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

sparkContext = spark.sparkContext
sqlCon = spark.sqlContext

sqlContext = spark.sql

print("First SparkContext:")
print("APP Name: " + sparkContext.appName)
print("Deploy Mode: " + sparkContext.deployMode)
print("Master: " + sparkContext.master)

sparkSession2 = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExample-test") \
    .getOrCreate()

print("Second SparkContext:")
print("APP Name: " + sparkSession2.sparkContext.appName)
print("Deploy Mode: " + sparkSession2.sparkContext.deployMode)
print("Master: " + sparkSession2.sparkContext.master)