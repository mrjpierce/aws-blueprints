import json
import boto3
import secrets
from datetime import datetime
from typing import Dict, Any

dynamodb = boto3.resource('dynamodb')

def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    try:
        body = json.loads(event.get('body', '{}'))
        original_url = body.get('originalUrl')
        
        if not original_url:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'originalUrl is required'})
            }
        
        # Generate short code
        short_code = secrets.token_hex(4)
        
        # Store in DynamoDB
        table = dynamodb.Table('url-shortener')
        table.put_item(Item={
            'shortCode': short_code,
            'originalUrl': original_url,
            'createdAt': datetime.utcnow().isoformat(),
            'clickCount': 0
        })
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'shortCode': short_code,
                'shortUrl': f"https://{event['requestContext']['domainName']}/{short_code}",
                'originalUrl': original_url
            })
        }
    except Exception as e:
        print(f'Error in shorten function: {e}')
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'Internal server error'})
        }
