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
from pyspark import SparkContext
import collections

sc = SparkContext.getOrCreate()

def unapply_JHashMapWrapper(jmap):
    return JHashMapWrapper(jmap)

def unapply_JHashSetWrapper(jset):
    return JHashSetWrapper(jset)

class JHashMapWrapper:
  def __init__(self, jmap):
    self.jmap = jmap
    
class JHashSetWrapper:
  def __init__(self, jset):
    self.jset = jset
  
map_data = [("one", 1), ("two", 2)]
rdd_map = sc.parallelize(map_data)
map = collections.OrderedDict(rdd_map.collect())
set = set(map.keys())

# Works:
jmap = unapply_JHashMapWrapper(map).jmap
jset = unapply_JHashSetWrapper(set).jset
print("Match with JHashMapWrapper", jmap)
print("Match with JHashSetWrapper", jset)

# Fails to compile because there are _two_ possible returned values.
for x in [map, set]:
  if isinstance(unapply_JHashMapWrapper(x), JHashMapWrapper):
    print('Match with JHashMapWrapper', unapply_JHashMapWrapper(x).jmap)
  elif isinstance(unapply_JHashSetWrapper(x), JHashSetWrapper):
    print('Match with JHashSetWrapper', unapply_JHashSetWrapper(x).jset)