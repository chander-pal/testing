# Scala code:
# // src/script/scala/progscala3/collections/MutableCollections.scala
# import collection.mutable.ArrayBuffer
# 
# val seq = ArrayBuffer(0)
# 
# seq ++=  Seq(1, 2)               // Alias for appendAll
# seq.appendAll(Seq(3, 4))         // Append a sequence
# seq += 5                         // Alias for addOne
# seq.addOne(6)                    // Append one element
# seq.append(7)                    // Append one element
# assert(seq == ArrayBuffer(0, 1, 2, 3, 4, 5, 6, 7))
# 
# Seq(-2, -1) ++=: seq             // Alias for prependAll
# seq.prependAll(Seq(-4, -3))      // Prepend a sequence
# -5 +=: seq                       // Alias for prepend
# seq.prepend(-6)                  // Prepend one element
# assert(seq == ArrayBuffer(-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7))
# 
# seq -= -6                        // Alias for subtractOne
# seq.subtractOne(7)               // Remove the element
# seq --= Seq(-2, -4)              // Alias for subtractAll
# seq.subtractAll(Seq(2, 4))       // Remove a sequence
# assert(seq == ArrayBuffer(-5, -3, -1, 0, 1, 3, 5, 6))
# 

# PySpark equivalent provided by GPT:
import pyspark.sql.functions as F

# Dummy PySpark code
spark = SparkSession.builder.appName('example').getOrCreate()

# Read data from a CSV file
df = spark.read.csv('data.csv', header=True)

# Show the first 5 rows
df.show(5)

# Perform a simple transformation
df_transformed = df.withColumn('new_column', F.col('old_column') + 1)

# Show the transformed data
df_transformed.show(5)

# Write the transformed data to a Parquet file
df_transformed.write.parquet('output.parquet')

# Stop the Spark session
spark.stop()