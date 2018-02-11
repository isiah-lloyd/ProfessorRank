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
      body = {
        "id": professor[0],
        "name": professor[1],
        "school_id": professor[2], #TODO: When School methods are implemented, join tables so school data is returned instead of school_id
        "department": professor[3]
        "rating": professor[4],
      }
      response = {
        "statusCode": 200,
        "body": json.dumps(body)
      }
    return response
def createReview(event, context):
    http_body = json.loads(event['body'])
    db_connection.createReview()
    return response
def getReview(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
if __name__ == "__main__":
    createProfessor('', '')