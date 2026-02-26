from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, to_timestamp

def run(input_path: str) -> None:
    spark = SparkSession.builder.appName("CyberLogBatch").getOrCreate()
    df = spark.read.json(input_path)

    clean = (
        df.withColumn("event_time", to_timestamp(col("timestamp")))
          .withColumn("severity", col("severity"))
          .filter(col("event_time").isNotNull())
    )

    agg = clean.groupBy("severity", "event").agg(count("*").alias("event_count"))
    agg.orderBy(col("event_count").desc()).show(truncate=False)
    spark.stop()

if __name__ == "__main__":
    run("logs.json")
