# Scala code:
# # Scala code:
# # # Scala code:
# # # // src/script/scala/progscala3/patternmatching/UnapplySingleValue2.scala
# # # 
# # # import java.util.{HashMap as JHashMap, HashSet as JHashSet}
# # # 
# # # case class JHashMapWrapper[K,V](jmap: JHashMap[K,V])
# # # object JHashMapWrapper:
# # #   def unapply[K,V](map: Map[K,V]): JHashMapWrapper[K,V] =
# # #     val jmap = new JHashMap[K,V]()
# # #     for (k,v) <- map do jmap.put(k, v)
# # #     new JHashMapWrapper(jmap)
# # # 
# # # case class JHashSetWrapper[K](jset: JHashSet[K])
# # # object JHashSetWrapper:
# # #   def unapply[K](set: Set[K]): JHashSetWrapper[K] =
# # #     val jset = new JHashSet[K]()
# # #     for k <- set do jset.add(k)
# # #     JHashSetWrapper(jset)
# # # 
# # # val map = Map("one" -> 1, "two" -> 2)
# # # val set = map.keySet
# # # 
# # # // Works:
# # # map match
# # #   case JHashMapWrapper(jmap) => jmap
# # # set match
# # #   case JHashSetWrapper(jset) => jset
# # # 
# # # // This fails to compile because there are _two_ possible returned values.
# # # for x <- Seq(map, set) yield x match
# # #   case JHashMapWrapper(jmap) => jmap
# # #   case JHashSetWrapper(jset) => jset
# # # 
# # 
# # # PySpark equivalent provided by GPT:
# # from pyspark.sql import SparkSession
# # from typing import TypeVar
# # 
# # K = TypeVar('K')
# # V = TypeVar('V')
# # 
# # class JHashMapWrapper:
# #     def __init__(self, jmap):
# #         self.jmap = jmap
# # 
# #     @staticmethod
# #     def unapply(map):
# #         jmap = {}
# #         for k, v in map.items():
# #             jmap[k] = v
# #         return JHashMapWrapper(jmap)
# # 
# # class JHashSetWrapper:
# #     def __init__(self, jset):
# #         self.jset = jset
# # 
# #     @staticmethod
# #     def unapply(s):
# #         jset = set(s)
# #         return JHashSetWrapper(jset)
# # 
# # map = {"one": 1, "two": 2}
# # set = set(map.keys())
# # 
# # # Works:
# # if isinstance(map, dict):
# #     jmap = JHashMapWrapper.unapply(map).jmap
# # if isinstance(set, set):
# #     jset = JHashSetWrapper.unapply(set).jset
# # 
# # # This fails to compile because there are _two_ possible returned values.
# # for x in [map, set]:
# #     if isinstance(x, dict):
# #         jmap = JHashMapWrapper.unapply(x).jmap
# #     if isinstance(x, set):
# #         jset = JHashSetWrapper.unapply(x).jset
# 
# # PySpark equivalent provided by GPT:
# # PySpark equivalent provided by GPT:
# from pyspark.sql import SparkSession
# 
# class JHashMapWrapper:
#     def __init__(self, jmap):
#         self.jmap = jmap
# 
#     @staticmethod
#     def unapply(map):
#         jmap = {}
#         for k, v in map.items():
#             jmap[k] = v
#         return JHashMapWrapper(jmap)
# 
# class JHashSetWrapper:
#     def __init__(self, jset):
#         self.jset = jset
# 
#     @staticmethod
#     def unapply(s):
#         jset = set(s)
#         return JHashSetWrapper(jset)
# 
# map = {"one": 1, "two": 2}
# set = set(map.keys())
# 
# # Works:
# if isinstance(map, dict):
#     jmap = JHashMapWrapper.unapply(map).jmap
# if isinstance(set, set):
#     jset = JHashSetWrapper.unapply(set).jset
# 
# # This fails to compile because there are _two_ possible returned values.
# for x in [map, set]:
#     if isinstance(x, dict):
#         jmap = JHashMapWrapper.unapply(x).jmap
#     if isinstance(x, set):
#         jset = JHashSetWrapper.unapply(x).jset

# PySpark equivalent provided by GPT:
from pyspark.sql import SparkSession

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
    def unapply(s):
        jset = set(s)
        return JHashSetWrapper(jset)

map = {"one": 1, "two": 2}
set = set(map.keys())

# Works:
if isinstance(map, dict):
    jmap = JHashMapWrapper.unapply(map).jmap
if isinstance(set, set):
    jset = JHashSetWrapper.unapply(set).jset

# This fails to compile because there are _two_ possible returned values.
for x in [map, set]:
    if isinstance(x, dict):
        jmap = JHashMapWrapper.unapply(x).jmap
    if isinstance(x, set):
        jset = JHashSetWrapper.unapply(x).jset