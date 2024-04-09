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
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark Session
spark = SparkSession.builder.getOrCreate()

seq_df = spark.createDataFrame([(0, )], ["value"])  # Creating DataFrame from ArrayBuffer like sequence (0)

addition_data = [(1, ), (2, ), (3, ), (4, ), (5, ), (6, ), (7, )]  
seq_df = seq_df.unionAll([spark.createDataFrame(addition_data, ["value"])])  # Append a sequence to DataFrame

prepend_data = [(-2, ), (-1, )]   
seq_df = spark.createDataFrame(prepend_data).unionAll(seq_df)   # Alias for prependAll

prepend_single_data = [(-3, ), (-4, )] 
for data in prepend_single_data:   # Prepend one element to DataFrame
    seq_df = spark.createDataFrame([data], ["value"]).unionAll(seq_df)
    
assert (seq_df.sort(col("value").asc()).collect() == [row['value'] for row in addition_data + prepend_data + prepend_single_data])

removal_data = [-6, 7]    # Alias for subtractOne and remove the element
seq_df = seq_df.filter(~col("value").isin(removal_data))   # Remove elements from DataFrame

subtraction_data = [-2, -4, 2, 4]  
seq_df = seq_df.filter(~col("value").isin(subtraction_data))   # Alias for subtractAll and remove sequence

assert (seq_df.sort(col("value").asc()).collect() == [-5, -3, -1, 0, 1, 3, 5, 6])