import json


def getting_started(event, context):
    body = {
        "message": "Go Serverless v3.0! Getting Started with Serverless \
             execution!",
        "event": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
