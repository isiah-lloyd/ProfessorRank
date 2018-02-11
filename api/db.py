import psycopg2
import psycopg2.extras
import os
class DBconnection():
  def __init__(self):
    DATABASE_NAME = os.environ['DB_NAME']
    DATABASE_USER_NAME = os.environ['DB_USER_NAME']
    DATABASE_PASSWORD = os.environ['DB_PASSWORD']
    DATABASE_HOST = os.environ['DB_HOST']
    DATABASE_PORT = os.environ['DB_PORT']
    self.db_connection = psycopg2.connect(f'dbname={DATABASE_NAME} user={DATABASE_USER_NAME} password={DATABASE_PASSWORD} host={DATABASE_HOST} port={DATABASE_PORT}')
    self.cursor = self.db_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

  def createProfessor(self, name, school_id, department):
    self.cursor.execute("""INSERT INTO professors(name, school_id, department) VALUES(%s, %s, %s) RETURNING id""", (name, school_id, department))
    return self.cursor.fetchone()[0]

  def getProfessor(self, id):
    self.cursor.execute("""SELECT id, name, school_id, department, rating FROM professors WHERE id=%s LIMIT 1""", (id))
    return self.cursor.fetchone()

  def createReview(self, professor_id, user_id, rating, comment):
    self.cursor.execute("""INSERT INTO reviews(professor_id, user_id, rating, comment) VALUES(%s, %s, %s, %s)""", (professor_id, user_id, rating, comment))

  def getReview(self, id):
    self.cursor.execute("""SELECT id, user_id, rating, comment, created_at FROM reviews WHERE professor_id=%s LIMIT 10""", (id))
    return self.cursor.fetchall()

  def __del__(self):
    self.db_connection.commit()
    self.db_connection.close()
