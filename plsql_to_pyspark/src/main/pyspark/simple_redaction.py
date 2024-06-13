# src/main/pyspark/simple_redaction.py

from pyspark.sql.functions import col, when, substring, lit, udf
from pyspark.sql.types import StringType


def redaction_logic(input_str, price):
    if price > 100:
        return input_str[0] + "*****" + input_str[-1]
    else:
        return input_str


redaction_udf = udf(redaction_logic, StringType())


def simple_redaction(df):
    return df.withColumn("redacted_input", redaction_udf(col("input"), col("price")))
