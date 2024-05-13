import org.apache.spark.sql.SparkSession

object SparkInitializer {
  def initSpark(appName: String): SparkSession = {
    SparkSession.builder()
      .appName(appName)
      .getOrCreate()
  }
}
