from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext, Row

##spark  = SparkSession.builder.master("local").appName("AppName").getOrCreate()
movies = spark.read.csv("movies.csv", header=True, mode= "DROPMALFORMED")

print (movies)
print (type (movies))
print (type (movies.first()))
print (movies.fist())
print (movies.count())
print (movies.head(n=5))