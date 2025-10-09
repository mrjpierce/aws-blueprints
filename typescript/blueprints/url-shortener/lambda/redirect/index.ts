import { APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, GetCommand, UpdateCommand } from '@aws-sdk/lib-dynamodb';

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
    const getResult = await docClient.send(new GetCommand({
      TableName: process.env.TABLE_NAME!,
      Key: { shortCode }
    }));
    
    if (!getResult.Item) {
      return {
        statusCode: 404,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ error: 'Short URL not found' })
      };
    }
    
    // Increment click count
    await docClient.send(new UpdateCommand({
      TableName: process.env.TABLE_NAME!,
      Key: { shortCode },
      UpdateExpression: 'SET clickCount = clickCount + :inc',
      ExpressionAttributeValues: { ':inc': 1 }
    }));
    
    return {
      statusCode: 302,
      headers: {
        'Location': getResult.Item.originalUrl,
        'Cache-Control': 'no-cache'
      },
      body: ''
    };
  } catch (error) {
    console.error('Error in redirect function:', error);
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ error: 'Internal server error' })
    };
  }
};
