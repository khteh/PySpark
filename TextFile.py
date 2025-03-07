from pyspark.sql.session import SparkSession
from pyspark.sql import functions as sf
from pathlib import Path
from utils.FileUtil import Download, Unzip, Rename
"""
https://spark.apache.org/docs/latest/quick-start.html
"""
def TextFiles(url, path):
    Download(url, Path(path))
    Unzip(Path(path), "/tmp")
    Rename(Path("/tmp/sentiment labelled sentences"), "/tmp/sentiment_data")
    return {
        'yelp': '/tmp/sentiment_data/yelp_labelled.txt',
        'amazon': '/tmp/sentiment_data/amazon_cells_labelled.txt',
        'imdb': '/tmp/sentiment_data/imdb_labelled.txt'
    }
   
def TextFileAnalysis(files):
    print(f"=== {TextFileAnalysis.__name__} ===")
    spark = SparkSession.builder.appName("TextFile").getOrCreate()
    yelp_text = spark.read.text(files["yelp"]).cache()
    print(f"{yelp_text.count()} rows")
    lines = yelp_text.filter(yelp_text.value.contains("What"))
    print(f"{lines.count()} lines which contain 'What'")
    spark.stop()

def DatasetOperations(files):
    """
    Maps a line to an integer value and aliases it as "words", creating a new DataFrame
    """
    print(f"\n=== {DatasetOperations.__name__} ===")
    spark = SparkSession.builder.appName("TextFile").getOrCreate()
    yelp_text = spark.read.text(files["yelp"]).cache()
    words = sf.split(yelp_text.value, " ")
    length = sf.size(words)
    words_df = yelp_text.select(length.name("words")) # argument is Column
    max_words = words_df.agg(sf.max(sf.col("words"))).collect() # argument is Column
    print(f"Largest words count: {max_words}")
    rows = sf.explode(words) # Transform dataset of lines to dataset of words
    words_df = yelp_text.select(rows.alias("word"))
    words_df = words_df.groupBy("word").count().collect()
    print("\nwords_df[:10]:")
    print(words_df[:10])
    spark.stop()

if __name__ == "__main__":
    files = TextFiles("https://archive.ics.uci.edu/ml/machine-learning-databases/00331/sentiment%20labelled%20sentences.zip", "/tmp/sentiment_data.zip")
    TextFileAnalysis(files)
    DatasetOperations(files)