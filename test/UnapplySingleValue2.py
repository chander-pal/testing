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
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("UnapplySingleValue2").getOrCreate()

class JHashMapWrapper:
    def __init__(self, jmap):
        self.jmap = jmap

    @staticmethod
    def unapply(map):
        jmap = {}
        for k, v in map.items():
            jmap[k] = v
        return JHashMapWrapper(jmap)

class JHashSetWrapper:
    def __init__(self, jset):
        self.jset = jset

    @staticmethod
    def unapply(set):
        jset = set.copy()
        return JHashSetWrapper(jset)

map = {"one": 1, "two": 2}
set = set(map.keys())

# Works:
jmap = JHashMapWrapper.unapply(map).jmap
jset = JHashSetWrapper.unapply(set).jset

# This fails to compile because there are _two_ possible returned values.
result = []
for x in [map, set]:
    if isinstance(x, dict):
        result.append(JHashMapWrapper.unapply(x).jmap)
    else:
        result.append(JHashSetWrapper.unapply(x).jset)

for r in result:
    print(r)