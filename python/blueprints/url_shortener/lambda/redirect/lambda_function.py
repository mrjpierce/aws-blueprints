import json
import boto3
from typing import Dict, Any

dynamodb = boto3.resource('dynamodb')

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    try:
        short_code = event.get('pathParameters', {}).get('shortCode')
        
        if not short_code:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'shortCode is required'})
            }
        
        # Get item from DynamoDB
        table = dynamodb.Table('url-shortener')
        response = table.get_item(Key={'shortCode': short_code})
        
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Short URL not found'})
            }
        
        # Increment click count
        table.update_item(
            Key={'shortCode': short_code},
            UpdateExpression='SET clickCount = clickCount + :inc',
            ExpressionAttributeValues={':inc': 1}
        )
        
        return {
            'statusCode': 302,
            'headers': {
                'Location': response['Item']['originalUrl'],
                'Cache-Control': 'no-cache'
            },
            'body': ''
        }
    except Exception as e:
        print(f'Error in redirect function: {e}')
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'Internal server error'})
        }
