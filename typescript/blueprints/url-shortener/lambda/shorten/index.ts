import { APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, PutCommand } from '@aws-sdk/lib-dynamodb';
import { randomBytes } from 'crypto';

const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);

export const handler = async (
  event: APIGatewayProxyEvent
): Promise<APIGatewayProxyResult> => {
  try {
    const { originalUrl } = JSON.parse(event.body || '{}');
    
    if (!originalUrl) {
      return {
        statusCode: 400,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ error: 'originalUrl is required' })
      };
    }
    
    // Generate short code
    const shortCode = generateShortCode();
    
    // Store in DynamoDB
    await docClient.send(new PutCommand({
      TableName: process.env.TABLE_NAME!,
      Item: {
        shortCode,
        originalUrl,
        createdAt: new Date().toISOString(),
        clickCount: 0
      }
    }));
    
    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        shortCode,
        shortUrl: `https://${event.requestContext.domainName}/${shortCode}`,
        originalUrl
      })
    };
  } catch (error) {
    console.error('Error in shorten function:', error);
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ error: 'Internal server error' })
    };
  }
};

function generateShortCode(): string {
  return randomBytes(4).toString('hex');
}
