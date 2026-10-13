import sqlite3
import os

database_dir = 'database'

path = os.path.join(os.getcwd(),database_dir)

if not os.path.exists(path):
  os.mkdir(path)

database = r'database/liberary.db'