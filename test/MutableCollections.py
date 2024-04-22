# Scala code:
# # Scala code:
# # # Scala code:
# # # # Scala code:
# # # # # Scala code:
# # # # # // src/script/scala/progscala3/collections/MutableCollections.scala
# # # # # import collection.mutable.ArrayBuffer
# # # # # 
# # # # # val seq = ArrayBuffer(0)
# # # # # 
# # # # # seq ++=  Seq(1, 2)               // Alias for appendAll
# # # # # seq.appendAll(Seq(3, 4))         // Append a sequence
# # # # # seq += 5                         // Alias for addOne
# # # # # seq.addOne(6)                    // Append one element
# # # # # seq.append(7)                    // Append one element
# # # # # assert(seq == ArrayBuffer(0, 1, 2, 3, 4, 5, 6, 7))
# # # # # 
# # # # # Seq(-2, -1) ++=: seq             // Alias for prependAll
# # # # # seq.prependAll(Seq(-4, -3))      // Prepend a sequence
# # # # # -5 +=: seq                       // Alias for prepend
# # # # # seq.prepend(-6)                  // Prepend one element
# # # # # assert(seq == ArrayBuffer(-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7))
# # # # # 
# # # # # seq -= -6                        // Alias for subtractOne
# # # # # seq.subtractOne(7)               // Remove the element
# # # # # seq --= Seq(-2, -4)              // Alias for subtractAll
# # # # # seq.subtractAll(Seq(2, 4))       // Remove a sequence
# # # # # assert(seq == ArrayBuffer(-5, -3, -1, 0, 1, 3, 5, 6))
# # # # # 
# # # # 
# # # # # PySpark equivalent provided by GPT:
# # # # from pyspark.sql import SparkSession
# # # # from pyspark.sql import Row
# # # # from pyspark.sql.functions import col
# # # # 
# # # # spark = SparkSession.builder.appName("MutableCollections").getOrCreate()
# # # # 
# # # # seq = [0]
# # # # 
# # # # seq.extend([1, 2])               # Alias for appendAll
# # # # seq.extend([3, 4])               # Append a sequence
# # # # seq.append(5)                    # Alias for addOne
# # # # seq.append(6)                    # Append one element
# # # # seq.append(7)                    # Append one element
# # # # assert seq == [0, 1, 2, 3, 4, 5, 6, 7]
# # # # 
# # # # seq = [-2, -1] + seq             # Alias for prependAll
# # # # seq = [-4, -3] + seq             # Prepend a sequence
# # # # seq.insert(0, -5)                # Alias for prepend
# # # # seq.insert(0, -6)                # Prepend one element
# # # # assert seq == [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
# # # # 
# # # # seq.remove(-6)                   # Alias for subtractOne
# # # # seq.remove(7)                    # Remove the element
# # # # seq = [x for x in seq if x not in [-2, -4]]  # Alias for subtractAll
# # # # seq = [x for x in seq if x not in [2, 4]]     # Remove a sequence
# # # # assert seq == [-5, -3, -1, 0, 1, 3, 5, 6]
# # # 
# # # # PySpark equivalent provided by GPT:
# # # # PySpark equivalent
# # # from pyspark.sql import SparkSession
# # # 
# # # spark = SparkSession.builder.appName("MutableCollections").getOrCreate()
# # # 
# # # seq = [0]
# # # 
# # # seq.extend([1, 2])               # Alias for appendAll
# # # seq.extend([3, 4])               # Append a sequence
# # # seq.append(5)                    # Alias for addOne
# # # seq.append(6)                    # Append one element
# # # seq.append(7)                    # Append one element
# # # assert seq == [0, 1, 2, 3, 4, 5, 6, 7]
# # # 
# # # seq = [-2, -1] + seq             # Alias for prependAll
# # # seq = [-4, -3] + seq             # Prepend a sequence
# # # seq.insert(0, -5)                # Alias for prepend
# # # seq.insert(0, -6)                # Prepend one element
# # # assert seq == [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
# # # 
# # # seq.remove(-6)                   # Alias for subtractOne
# # # seq.remove(7)                    # Remove the element
# # # seq = [x for x in seq if x not in [-2, -4]]  # Alias for subtractAll
# # # seq = [x for x in seq if x not in [2, 4]]     # Remove a sequence
# # # assert seq == [-5, -3, -1, 0, 1, 3, 5, 6]
# # 
# # # PySpark equivalent provided by GPT:
# # from pyspark.sql import SparkSession
# # 
# # spark = SparkSession.builder.appName("MutableCollections").getOrCreate()
# # 
# # seq = [0]
# # 
# # seq.extend([1, 2])               # Alias for appendAll
# # seq.extend([3, 4])               # Append a sequence
# # seq.append(5)                    # Alias for addOne
# # seq.append(6)                    # Append one element
# # seq.append(7)                    # Append one element
# # assert seq == [0, 1, 2, 3, 4, 5, 6, 7]
# # 
# # seq = [-2, -1] + seq             # Alias for prependAll
# # seq = [-4, -3] + seq             # Prepend a sequence
# # seq.insert(0, -5)                # Alias for prepend
# # seq.insert(0, -6)                # Prepend one element
# # assert seq == [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
# # 
# # seq.remove(-6)                   # Alias for subtractOne
# # seq.remove(7)                    # Remove the element
# # seq = [x for x in seq if x not in [-2, -4]]  # Alias for subtractAll
# # seq = [x for x in seq if x not in [2, 4]]     # Remove a sequence
# # assert seq == [-5, -3, -1, 0, 1, 3, 5, 6]
# 
# # PySpark equivalent provided by GPT:
# # PySpark equivalent
# from pyspark.sql import SparkSession
# 
# spark = SparkSession.builder.appName("MutableCollections").getOrCreate()
# 
# seq = sc.parallelize([0])
# 
# seq = seq.union(sc.parallelize([1, 2]))  # Alias for appendAll
# seq = seq.union(sc.parallelize([3, 4]))  # Append a sequence
# seq = seq.union(sc.parallelize([5]))     # Alias for addOne
# seq = seq.union(sc.parallelize([6]))     # Append one element
# seq = seq.union(sc.parallelize([7]))     # Append one element
# assert seq.collect() == [0, 1, 2, 3, 4, 5, 6, 7]
# 
# seq = sc.parallelize([-2, -1]).union(seq)  # Alias for prependAll
# seq = sc.parallelize([-4, -3]).union(seq)  # Prepend a sequence
# seq = sc.parallelize([-5]).union(seq)      # Alias for prepend
# seq = sc.parallelize([-6]).union(seq)      # Prepend one element
# assert seq.collect() == [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
# 
# seq = seq.filter(lambda x: x != -6)       # Alias for subtractOne
# seq = seq.filter(lambda x: x != 7)        # Remove the element
# seq = seq.filter(lambda x: x not in [-2, -4])  # Alias for subtractAll
# seq = seq.filter(lambda x: x not in [2, 4])     # Remove a sequence
# assert seq.collect() == [-5, -3, -1, 0, 1, 3, 5, 6]

# PySpark equivalent provided by GPT:
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MutableCollections").getOrCreate()

seq = sc.parallelize([0])

seq = seq.union(sc.parallelize([1, 2]))  # Alias for appendAll
seq = seq.union(sc.parallelize([3, 4]))  # Append a sequence
seq = seq.union(sc.parallelize([5]))     # Alias for addOne
seq = seq.union(sc.parallelize([6]))     # Append one element
seq = seq.union(sc.parallelize([7]))     # Append one element
assert seq.collect() == [0, 1, 2, 3, 4, 5, 6, 7]

seq = sc.parallelize([-2, -1]).union(seq)  # Alias for prependAll
seq = sc.parallelize([-4, -3]).union(seq)  # Prepend a sequence
seq = sc.parallelize([-5]).union(seq)      # Alias for prepend
seq = sc.parallelize([-6]).union(seq)      # Prepend one element
assert seq.collect() == [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]

seq = seq.filter(lambda x: x != -6)       # Alias for subtractOne
seq = seq.filter(lambda x: x != 7)        # Remove the element
seq = seq.filter(lambda x: x not in [-2, -4])  # Alias for subtractAll
seq = seq.filter(lambda x: x not in [2, 4])     # Remove a sequence
assert seq.collect() == [-5, -3, -1, 0, 1, 3, 5, 6]