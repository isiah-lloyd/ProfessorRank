#Required code for serverless-python-requirements to zip dependencies
try:
  import unzip_requirements
except ImportError:
  pass
#####################################################################

import json
import db

def createProfessor(event, context):
    http_body = json.loads(event['body'])
    db_connection = db.DBconnection()
    createdProfessorID = db_connection.createProfessor(http_body['name'], http_body['school_id'], http_body['department'])
    body = {
        "id": createdProfessorID
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def getProfessor(event, context):
    db_connection = db.DBconnection()
    professor = db_connection.getProfessor(event['pathParameters']['id'])
    if not professor:
      body = {
        "error": "Professor ID does not exist"
      }
      response = {
        "statusCode": 404,
        "body": json.dumps(body)
      }
    else:
      response = {
        "statusCode": 200,
        "body": json.dumps(professor)
      }
    return response
def createReview(event, context):
    http_body = json.loads(event['body'])
    db_connection = db.DBconnection()
    db_connection.createReview(http_body['professor_id'], http_body['user_id'], http_body['rating'], http_body['comment'])
    response = {
        "statusCode": 200,
    }
    return response
def getReview(event, context):
    db_connection = db.DBconnection()
    reviews = db_connection.getProfessor(event['pathParameters']['id'])
    if not review:
      body = {
        "error": "No reviews for professor"
      }
      response = {
        "statusCode": 404,
        "body": json.dumps(body)
      }
    else:
      response = {
        "statusCode": 200,
        "body": json.dumps(reviews)
      }
    return response
if __name__ == "__main__":
    createProfessor('', '')