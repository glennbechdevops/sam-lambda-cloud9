import os
import json
import boto3
from UnleashClient import UnleashClient

def handler(event, context):

# Initialize the Unleash client and the boto3 client to interact with
# AWS and the Unleash feature toggle service.

    unleash_client = UnleashClient(
        url="https://eu.app.unleash-hosted.com/eubb1043/api",
        app_name="sentiment",
        cache_directory="/tmp/",
        custom_headers={'Authorization': os.environ['UnleashToken']})

    unleash_client.initialize_client()

    client = boto3.client('comprehend')

## Process sentiment analysis onlyif the MOCK toggle is ON. Mock returns very Positive sentiment just in case
    body = event["body"]

    if unleash_client.is_enabled("MOCK"):
        sentiment = {
            "Sentiment": "POSITIVE",
            "SentimentScore": {
                "Positive": 0.9974453449249268,
                "Negative": 0.0074453449249268,
                "Neutral": 0.00039782875683158636,
                "Mixed": 0.0019206495489925146
            }
        }
    else:
        sentiment = client.detect_sentiment(LanguageCode = "en", Text = body)

    return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "sentiment ": json.dumps(sentiment)
            })
        }