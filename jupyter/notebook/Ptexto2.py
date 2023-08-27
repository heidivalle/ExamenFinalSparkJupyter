from pyspark import SparkContext
from operator import add
sc= SparkContext("local[+]","My app")
rdd= sc.textFile("/dataset/yahoo-symbols-201709.csv")
def tokenize(text): return text.split()
histograma_palabras=rdd. flatiap(tokenize)
histograma_palabras=histograma_palabras.map(lambda x:(x,1)).reduceByKey(add).collectAsMap()
print(histograma_palabras)

