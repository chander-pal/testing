package com.sparkbyexamples.spark

import org.apache.spark.sql.{SQLContext, SparkSession}

object SQLContextExample extends App {

  val spark = SparkSession.builder()
    .master("local[1]")
    .appName("SparkByExamples.com")
    .getOrCreate();

  spark.sparkContext.setLogLevel("ERROR")

