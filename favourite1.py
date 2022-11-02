import csv
import sqlite3

# way to create a empty file
open("shows.db","w").close() # -> opening and closing and file

db = sqlite3.connect("shows.db") # connecting sqlite3 to the database

c = db.cursor()

# db.execute("CREATE TABLE IF NOT EXISTS shows (id INTEGER,title TEXT,PRIMARY KEY(id))")
# db.execute("CREATE TABLE IF NOT EXISTS genres (show_id INTEGER,genre TEXT,FOREIGN KEY(show_id) REFERENCES shows(id)")
# db.execute("DROP TABLE shows")
# db.execute("DROP TABLE genres")

c.execute("CREATE TABLE shows (id INTEGER ,title STRING,PRIMARY KEY(id))")
c.execute("CREATE TABLE genres (id INTEGER,genre TEXT,FOREIGN KEY(id) REFERENCES shows(id))")

with open("top_movies.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["movie"].strip().upper()

        c.executemany("INSERT INTO shows (title) VALUES(?)",[title,])