# DROP TABLES
drop_input_texts = " DROP TABLE IF EXISTS input_texts"
drop_textsim_metrics = "DROP TABLE IF EXISTS textsim_metrics"

# CREATE TABLES

create_input_texts = """
  CREATE TABLE IF NOT EXISTS input_texts(
    table_id INT IDENTITY(1, 1) NOT NULL,
    text_id VARCHAR NOT NULL,
    text_name VARCHAR,
    total_words INT,
    unique_words INT,
    total_words_cleaned INT,
    unique_words_cleaned INT,
    ingestion_time DATETIME2
  )
"""

create_textsim_metrics = """
  CREATE TABLE IF NOT EXISTS textsim_metrics (
    ts_id INT IDENTITY(1, 1) NOT NULL,
    text_id_1 VARCHAR NOT NULL,
    text_name_1 VARCHAR,
    text_id_2 VARCHAR,
    jaccard_similarity NUMERIC(10, 5),
    cosine_similarity NUMERIC(10, 5)
  )
"""


drop_table_queries = [drop_input_texts, drop_textsim_metrics]
create_table_queries = [create_input_texts, create_textsim_metrics]