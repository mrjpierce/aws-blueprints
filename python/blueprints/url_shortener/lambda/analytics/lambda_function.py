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
        
        item = response['Item']
        
        # Convert Decimal to int for JSON serialization
        click_count = item.get('clickCount', 0)
        if hasattr(click_count, 'to_integral_value'):
            click_count = int(click_count.to_integral_value())
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'shortCode': item['shortCode'],
                'originalUrl': item['originalUrl'],
                'clickCount': click_count,
                'createdAt': item['createdAt']
            })
        }
    except Exception as e:
        print(f'Error in analytics function: {e}')
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'Internal server error'})
        }
