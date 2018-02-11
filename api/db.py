import psycopg2
from os import environ
class DBconnection():
  DATABASE_NAME = os.environ['DB_NAME']
  DATABASE_USER_NAME = os.environ['DB_USER_NAME']
  DATABASE_PASSWORD = os.environ['DB_PASSWORD']
  DATABASE_HOST = os.environ['DB_HOST']
  DATABASE_PORT = os.environ['DB_PORT']
  def __init__(self):
    self.db_connection = psycopg2.connect(f'dbname={DATABASE_NAME} user={DATABASE_USER_NAME} password={DATABASE_PASSWORD} host={DATABASE_HOST} port={DATABASE_PORT}')
    self.cursor = db.db_connection.cursor()

  def __del__(self):
    self.cursor.close()
    self.db_connection.close()
