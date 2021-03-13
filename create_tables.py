import psycopg2
import os

from sql_queries import drop_table_queries, create_table_queries
from config import PGHOST, PGDBNAME, PGUSERNAME, PGPASSWORD

def drop_tables(conn, cursor):
  try:
    for query in drop_table_queries:
      cursor.execute(query)
      conn.commit()
    print('Tables dropped successfully!')
  except Exception as e:
    print(e)

def create_tables(conn, cursor):
  try:
    for query in create_table_queries:
      cursor.execute(query)
      conn.commit()
    print('Tables created successfully!')
  except Exception as e:
    print(e)

def main():
  conn = psycopg2.connect(
      user=PGUSERNAME,
      password=PGPASSWORD,
      host=PGHOST,
      database=PGDBNAME
  )

  cur = conn.cursor()

  drop_tables(conn, cur)
  create_tables(conn, cur)

  conn.close()

if __name__ == '__main__':

  main()










