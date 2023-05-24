import logging
import uuid
import json
import azure.functions as func

def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        qoute = req_body.get('name')

    if qoute:
        qoute_data=json.loads(qoute)
        newdocs = func.DocumentList() 
        newqoute_dict = {
            "qoute": qoute_data['qoute'],
            "author": qoute_data['author']
        }
        newdocs.append(func.Document.from_dict(newqoute_dict))
        doc.set(newdocs)
        
        return func.HttpResponse(f"Hello, {qoute_data['author']}.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )