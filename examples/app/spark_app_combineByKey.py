from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("spark_app_combineByKey")

sc = SparkContext(conf=conf)


def createCombiner(val):
    return [val]


def mergeValue(l, val):
    l.append(val)


def mergeCombiners(l, r):
    l.extend(r)

datas = sc.parallelize([("a", 1), ("a", 2), ("b", 1)]).combineByKey(
    createCombiner, mergeValue, mergeCombiners).collect()

sc.stop()
