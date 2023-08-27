
from pyspark import Sparkcontext
from operator import add

sc= SpawnContext("local[*]" , "My app")

rdd=sc.textFile("/dataset/yahoo-symbols-201709.csv")

def estadisticas (line):
    return [("caracteres”", len(line)),("palabras", len(line.split())),("Lines”",1)]
print (rdd.flatMap(estadisticas).reduceByKey(lambda a,b: a+b).collectasMap())

