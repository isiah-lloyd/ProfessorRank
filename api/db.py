import psycopg2
import os
class DBconnection():
  def __init__(self):
    DATABASE_NAME = os.environ['DB_NAME']
    DATABASE_USER_NAME = os.environ['DB_USER_NAME']
    DATABASE_PASSWORD = os.environ['DB_PASSWORD']
    DATABASE_HOST = os.environ['DB_HOST']
    DATABASE_PORT = os.environ['DB_PORT']
    self.db_connection = psycopg2.connect(f'dbname={DATABASE_NAME} user={DATABASE_USER_NAME} password={DATABASE_PASSWORD} host={DATABASE_HOST} port={DATABASE_PORT}')
    self.cursor = self.db_connection.cursor()

  def createProfessor(self, name, school_id, department):
    self.cursor.execute("""INSERT INTO professors(name, school_id, department) VALUES (%s, %s, %s)""", (name, school_id, department))

  def __del__(self):
    self.db_connection.commit()
    self.cursor.close()
    self.db_connection.close()
