import sqlite3
import os

database_dir = 'database'

path = os.path.join(os.detcwd(),database_dir)

if not os.path.exists(path):
  os.makedir(path)
