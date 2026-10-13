import sqlite3
import os

database_dir = 'database'

path = os.path.join(os.getcwd(),database_dir)

if not os.path.exists(path):
  os.mkdir(path)

database = r'database/liberary.db'

def create_db():
  conn = sqlite3.connect(database)
  return conn

def create_table_books():
  conn = create_db()
  cursor = conn.cursor()

  cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
      book_id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      author TEXT NOT NULL,
      is_issued INTEGER NOT NULL DEFAULT 0,
      price REAL NOT NULL
    )
  """)

  cursor.commit()
  conn.close()

def insert_into_books(title, author, price):
  conn = create_db()
  cursor = conn.cursor()

  cursor.execute(" INSERT INTO books(title, author, price) VALUES (?, ?, ?) ", (title, author, price))

  conn.commit()
  conn.close()

def update_books(book_id, title, author, is_issued, price):
  conn = create_db()
  cursor = conn.cursor()

  cursor.execute("""
    UPDATE books
    SET title = ?, author = ?, is_issued = ?, price = ?
    WHERE book_id = ? """, (title, author, is_issued, price, book_id))

  conn.commit()
  conn.close()

def delete_book(book_id):
  conn = create_db()
  cursor = conn.cursor()

  cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id))

  conn.commit()
  conn.close()

def create_table_members():
  conn = create_db()
  cursor = conn.cursor()

  cursor.execute("""
    CREATE TABLE IS NOT EXISTS members(
      member_id INTERGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT NOT NULL,
      number INTERGER NOT NULL
    )
  """)

  conn.commit()
  conn.close()

def insert_into_members(name, email, number):
  conn = create_db()
  cursor = conn.cursor()
  
  cursor.execute("INSERT INTO memebers(name, email, number) VALUES(?, ?, ?)", (name, email, number))

  conn.commit()
  conn.close()

def update_members(member_id, name, email, number):
  conn = create_db()
  cursor = conn.cursor()

  cursor.execute("""
    UPDATE books
    SET name = ?, email = ?, number = ?
    WHERE member_id = ? """, (name, email, number, member_id))

  conn.commit()
  conn.close()

def delete_book(member_id):
  conn = create_db()
  cursor = conn.cursor()

  cursor.execute("DELETE FROM members WHERE member_id = ?", (member_id))

  conn.commit()
  conn.close()