# Scala code:
# 
# import SparkInitializer.initSpark
# import org.apache.spark.sql.{SparkSession, Row}
# import org.apache.spark.sql.types.{StructType, StructField, StringType, IntegerType}
# 
# object MySparkJob {
#   def main(args: Array[String]): Unit = {
#     val spark = initSpark("MySparkJob")
# 
#     val schema = StructType(Seq(StructField("name", StringType, true), StructField("age", IntegerType, true)))
#     val data = Seq(("Alice", 34), ("Bob", 45), ("Charlie", 30))
#     val rdd = spark.sparkContext.parallelize(data)
#     val df = spark.createDataFrame(rdd.map { case (name, age) => Row(name, age) }, schema)
# 
#     df.show()
# 
#   }
# }
# MySparkJob.main(Array())

# PySpark equivalent provided by GPT:
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.appName("MySparkJob").getOrCreate()

data = [("Alice", 34), ("Bob", 45), ("Charlie", 30)]
schema = StructType([StructField("name", StringType(), True), StructField("age", IntegerType(), True)])

df = spark.createDataFrame(data, schema)

df.show()