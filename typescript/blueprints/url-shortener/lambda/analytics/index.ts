import { APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, GetCommand } from '@aws-sdk/lib-dynamodb';

const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);

export const handler = async (
  event: APIGatewayProxyEvent
): Promise<APIGatewayProxyResult> => {
  try {
    const shortCode = event.pathParameters?.shortCode;
    
    if (!shortCode) {
      return {
        statusCode: 400,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ error: 'shortCode is required' })
      };
    }
    
    // Get item from DynamoDB
    const result = await docClient.send(new GetCommand({
      TableName: process.env.TABLE_NAME!,
      Key: { shortCode }
    }));
    
    if (!result.Item) {
      return {
        statusCode: 404,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ error: 'Short URL not found' })
      };
    }
    
    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        shortCode: result.Item.shortCode,
        originalUrl: result.Item.originalUrl,
        clickCount: result.Item.clickCount || 0,
        createdAt: result.Item.createdAt
      })
    };
  } catch (error) {
    console.error('Error in analytics function:', error);
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ error: 'Internal server error' })
    };
  }
};
