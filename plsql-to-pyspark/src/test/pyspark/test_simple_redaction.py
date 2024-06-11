# src/test/pyspark/test_simple_redaction.py

import pytest
from pyspark.sql import SparkSession
from src.main.pyspark.simple_redaction import simple_redaction


@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.appName("TestApp").getOrCreate()


def test_simple_redaction(spark):
    # Create a sample DataFrame
    data = [("ProductName", 150), ("AnotherProduct", 50), ("A", 150)]
    columns = ["input", "price"]
    df = spark.createDataFrame(data, columns)

    # Apply the redaction function
    result_df = simple_redaction(df)

    # Collect the results
    results = result_df.collect()

    # Assertions
    assert results[0]["redacted_input"] == "P*****e"
    assert results[1]["redacted_input"] == "AnotherProduct"
    assert results[2]["redacted_input"] == "A*****A"
