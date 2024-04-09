# Scala code:
# // src/script/scala/progscala3/patternmatching/UnapplySingleValue2.scala
# 
# import java.util.{HashMap as JHashMap, HashSet as JHashSet}
# 
# case class JHashMapWrapper[K,V](jmap: JHashMap[K,V])
# object JHashMapWrapper:
#   def unapply[K,V](map: Map[K,V]): JHashMapWrapper[K,V] =
#     val jmap = new JHashMap[K,V]()
#     for (k,v) <- map do jmap.put(k, v)
#     new JHashMapWrapper(jmap)
# 
# case class JHashSetWrapper[K](jset: JHashSet[K])
# object JHashSetWrapper:
#   def unapply[K](set: Set[K]): JHashSetWrapper[K] =
#     val jset = new JHashSet[K]()
#     for k <- set do jset.add(k)
#     JHashSetWrapper(jset)
# 
# val map = Map("one" -> 1, "two" -> 2)
# val set = map.keySet
# 
# // Works:
# map match
#   case JHashMapWrapper(jmap) => jmap
# set match
#   case JHashSetWrapper(jset) => jset
# 
# // This fails to compile because there are _two_ possible returned values.
# for x <- Seq(map, set) yield x match
#   case JHashMapWrapper(jmap) => jmap
#   case JHashSetWrapper(jset) => jset
# 

# PySpark equivalent provided by GPT:
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import collections

def unapply_JHashMapWrapper(data):
    jmap = collections.OrderedDict()
    for k,v in data:
        jmap[k]=v
    return JHashMapWrapper(jmap)

def unapply_JHashSetWrapper(data):
    jset = set()
    for item in data:
        jset.add(item)
    return JHashSetWrapper(jset)

class JHashMapWrapper():
    def __init__(self, jmap):
        self.jmap = jmap
        
class JHashSetWrapper():
    def __init__(self, jset):
        self.jset = jset

# Create a SparkSession
spark = SparkSession(SparkContext(SparkConf()))

data = [("one", 1), ("two", 2)]
rdd = spark.sparkContext.parallelize(data)

mapRDD = rdd.collectAsMap()
setRDD = set(mapRDD.keys())

# Works:
jmapWrapper = unapply_JHashMapWrapper(mapRDD.items())
print(jmapWrapper.jmap)

jsetWrapper = unapply_JHashSetWrapper(setRDD)
print(jsetWrapper.jset)

# This fails to compile because there are _two_ possible returned values.
for x in [mapRDD.items(), setRDD]:
    try:
        jmapWrapper = unapply_JHashMapWrapper(x)
        print(jmapWrapper.jmap)
    except Exception as e1:
        try:
            jsetWrapper = unapply_JHashSetWrapper(x)
            print(jsetWrapper.jset)
        except Exception as e2:
            pass