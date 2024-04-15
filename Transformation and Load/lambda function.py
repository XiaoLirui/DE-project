import boto3
import base64
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('de_project') # table name

def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        
        data_item = json.loads(payload, parse_float=Decimal)
        
        dynamodb_item = {
            's': data_item['s'], #  's' is the Partition Key of the DynamoDB table
            't': str(data_item['t']),
            'data': data_item  # We can store the entire data_item as an attribute
        }
        
        # Inserting data into a DynamoDB table
        response = table.put_item(Item=dynamodb_item)
        print(f"Record inserted: {dynamodb_item}")

    return f"Successfully processed {len(event['Records'])} records."
