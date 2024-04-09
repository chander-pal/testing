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
from pyspark import SparkContext
sc = SparkContext("local")

rdd = sc.parallelize([0])

# Append a sequence
seq1 = rdd.union(sc.parallelize([1, 2]))
seq1 = seq1.union(sc.parallelize([3, 4]))
seq1 = seq1.union(sc.parallelize([5]))
assert(seq1.collect() == [0, 1, 2, 3, 4, 5])

# Prepend a sequence
seq2 = sc.parallelize([-6, -5]).union(rdd)
seq2 = seq2.union(sc.parallelize([-4, -3]))
assert(seq2.collect() == [-6, -5, 0, -4, -3])

# Remove a sequence
seq3 = sc.parallelize([-6, -5]).subtract(rdd)
seq3 = seq3.subtract(sc.parallelize([-4, -3]))
seq3 = seq3.subtract(sc.parallelize([0, 1, 2, 3, 4]))
assert(seq3.collect() == [-5, 5])