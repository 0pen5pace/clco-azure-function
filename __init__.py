import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, doc:func.DocumentList) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')
 
    users_json = []

    for user in doc:
        qoute_json = {
           "author": user['author'],
           "qoute": user['qoute']
        }
        users_json.append(qoute_json)

    return func.HttpResponse(
            json.dumps(qoute_json),
            status_code=200,
            mimetype="application/json"            
    )