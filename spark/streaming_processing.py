from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, StringType

schema = StructType() \
    .add("user_id", StringType()) \
    .add("timestamp", StringType()) \
    .add("event", StringType()) \
    .add("severity", StringType()) \
    .add("src_ip", StringType()) \
    .add("dst_ip", StringType())

spark = SparkSession.builder.appName("CyberLogStreaming").getOrCreate()

raw = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
parsed = raw.select(from_json(col("value"), schema).alias("j")).select("j.*")

agg = parsed.groupBy(window(col("timestamp").cast("timestamp"), "5 minutes"), col("severity")).count()

query = agg.writeStream.outputMode("update").format("console").option("truncate", "false").start()
query.awaitTermination()
