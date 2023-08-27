from pyspark import SparkContext

sc = SparkContext("local[*]", "My app")

from pyspark.sql import SQLContext

sqlContext = SQLContext(sc)
dataframe = sqlContext.read.json("./data.json")
dataframe.printSchema()
dataframe.show()

dataframe.select("City").show()
dataframe.select("Country").show()
dataframe.select(dataframe['City'], dataframe['Country']+1).show()
dataframe.filter(dataframe['RecordNumber']>61391).show()

dataframe.registerTempTable ("DATA")
consulta=sqlContext.sql("SELECT * from DATA")
