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
    db_connection.createProfessor(http_body['name'], http_body['school_id'], http_body['department'])
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def getProfessor(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
def createReview(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

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