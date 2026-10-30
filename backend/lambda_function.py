import json
import os

import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ.get("TABLE_NAME", "DynamoDB-for-serverless-web-app"))


def lambda_handler(event, context):
    # Atomic increment: creates the item on the very first call and stays correct
    # when several visitors hit the page at the same moment.
    response = table.update_item(
        Key={"id": "1"},
        UpdateExpression="ADD #v :inc",
        ExpressionAttributeNames={"#v": "views"},
        ExpressionAttributeValues={":inc": 1},
        ReturnValues="UPDATED_NEW",
    )
    views = int(response["Attributes"]["views"])

    # CORS is configured on the Lambda Function URL itself, so no CORS headers here.
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(views),
    }
