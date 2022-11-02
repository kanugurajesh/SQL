import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
      conn = sqlite3.connect('shows.db')
      return conn
    except Error:
      print(Error)
 
def sql_table(conn, rows,genres):
    cursorObj = conn.cursor()
# Create the table
    cursorObj.execute("CREATE TABLE shows (id INTEGER ,title CHAR(30),PRIMARY KEY(id))")
    cursorObj.execute("CREATE TABLE genres (id INTEGER,genre TEXT,FOREIGN KEY(id) REFERENCES shows(id))")

    sqlite_insert_query = """INSERT INTO shows
                          (id, title) 
                          VALUES (?, ?);"""    

    sqlite_insert_genr_query = """INSERT INTO genres
                          (id, genre) 
                          VALUES (?, ?);"""

    cursorObj.executemany(sqlite_insert_query, rows)
    cursorObj.executemany(sqlite_insert_genr_query, genr)
    conn.commit()
    print("Number of records after inserting rows:")
    cursor = cursorObj.execute('select * from shows;')
    print(len(cursor.fetchall()))
  
# Insert records
rows = []
genr = []

import csv

with open("top_movies.csv","r") as file:
    reader = csv.DictReader(file)
    counter = 1
    for row in reader:
        title = row["movie"].strip().upper()
        number = row["num"].strip()
        rows.append((int(number),title))
        for genre in row["genres"].split(" "):
            genr.append((counter,genre))
        counter+=1

sqllite_conn = sql_connection() 
sql_table(sqllite_conn, rows,genr)
    
if (sqllite_conn):
  sqllite_conn.close()
  print("\nThe SQLite connection is closed.")