import psycopg2
import datetime
import time

import helperfunctions as hf
from config import PGHOST, PGDBNAME, PGUSERNAME, PGPASSWORD

def get_rowcount(conn, cursor):
  '''
    This function gets the rowcount from the input_texts table in postgres
    Input: connection object, cursor object from psycopg2
    Output: int
  '''
  cursor.execute("SELECT COUNT(*) FROM input_texts;")
  row_count = cursor.fetchone()
  return row_count[0]

def insert_texts(conn, cursor, texts:list):
  '''
    This function inserts all texts into the input_texts table in 
    your postgres DB. It loops through the list of texts and performs
    the data transformations such as creating unique text ids, word frequencies and stopword removal. 
    Then it inserts the transformed values into the table
    Input: connection object, cursor object from psycopg2, list of texts
    Output: a record in the input_texts table

  '''
  try:
    row_count = get_rowcount(conn, cursor)

    for text_file in texts:
      text_id = hf.zeropadder(row_count + 1, 8, 'TXT_')
      text_name = str(text_file).split('/')[-1]
      word_list = hf.transform_text(text_file)
      word_dict = hf.word_frequency(word_list)
      unique_words = hf.unique_word_count(word_dict)
      list_no_sw = hf.remove_stopwords(word_list)
      dict_no_sw = hf.word_frequency(list_no_sw)
      uw_no_sw = hf.unique_word_count(dict_no_sw)
      ingestion_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

      print('>>>>> Data transformations processed, starting inserts in table........')

      query =f"""
        INSERT INTO input_texts(text_id, text_name, total_words, unique_words, total_words_cleaned, unique_words_cleaned, ingestion_time)
        VALUES('{text_id}','{text_name}', {unique_words['total_words']}, {unique_words['unique_words']}, {uw_no_sw['total_words']}, {uw_no_sw['unique_words']}, '{ingestion_time}')
      """
      cursor.execute(query)
      row_count += 1
      print('>>>>> Record inserted successfully!')
      conn.commit()

  except Exception as e:
    print(e)


def insert_textsim_metrics(conn, cursor, text1, text2):
  '''
    This function inserts records in the textsim_metrics table in
    your postgres DB. It performs data transformations of 2 texts
    and calculates their similarity based on the jaccard similarity
    and cosine similarity.
    Input: connection object, cursor object from psycopg2, strings for text1 and text2
    Output: A record in your textsim_metrics table
  '''

  try:
    text_name_1 = str(text1).split('/')[-1]
    text_name_2 = str(text2).split('/')[-1]

    lst_1 = hf.remove_stopwords(hf.transform_text(text1))
    lst_2 = hf.remove_stopwords(hf.transform_text(text2))

    word_dict1 = hf.word_frequency(lst_1)
    word_dict2 = hf.word_frequency(lst_2)

    jaccard_similarity = hf.jaccard_similarity(lst_1, lst_2)
    cosine_similarity = hf.cosine_similarity(word_dict1, word_dict2)

    print('>>>>> Data transformations processed, starting inserts in table........')

    query = f"""
      INSERT INTO textsim_metrics(text_name_1, text_name_2, jaccard_similarity, cosine_similarity)
      VALUES('{text_name_1}', '{text_name_2}', {jaccard_similarity}, {cosine_similarity})
    """
    cursor.execute(query)
    print('>>>>> Record inserted successfully!')
    conn.commit()

  except Exception as e:
    print(e)


def main():

  try:
    conn = psycopg2.connect(
        user=PGUSERNAME,
        password=PGPASSWORD,
        host=PGHOST,
        database=PGDBNAME
    )

    cur = conn.cursor()
    sample1 = './sample_texts/sample_1.txt'
    sample2 = './sample_texts/sample_2.txt'
    sample3 = './sample_texts/sample_3.txt'
    sample_list = [sample1, sample2, sample3]

    print('STARTING DATA INGESTION input_texts.....')
    insert_texts(conn, cur, sample_list)
    print('DONE')

    time.sleep(4)
    
    print('STARTING DATA INGESTION textsim_metrics.....')
    insert_textsim_metrics(conn, cur, sample1, sample2)
    insert_textsim_metrics(conn, cur, sample1, sample3)
    insert_textsim_metrics(conn, cur, sample2, sample3)
    print('DONE')

  except Exception as e:
    print(e)

if __name__ == '__main__':
  
  main()