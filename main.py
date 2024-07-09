from googleapiclient.discovery import build
from dotenv import load_dotenv

import json
import os

load_dotenv()

yt_api_key = os.environ.get('YT_API_KEY')
assert yt_api_key, "YT_API_KEY is not set in .env file."
print(f'init: ENV YT_API_KEY: {yt_api_key}')


youtube_service = build('youtube', 'v3', developerKey=yt_api_key)

def v1(response):
    if 'itmes' in response:
        channel = response['items'][0]
        channel_id = channel['id']
        channel_title = channel['snippet']['title']
        subscriber_count = channel['statistics']['subscriberCount']
        view_count = channel['statistics']['viewCount']

        # Print the retrieved information
        print(f"Channel ID: {channel_id}")
        print(f"Channel Title: {channel_title}")
        print(f"Subscriber Count: {subscriber_count}")
        print(f"Total Views: {view_count}")
    else:
        print("No channel found.")

def call_yt(user='UCSI8iRkVKxEW1QRowCB_slg'):
    try:
        request = youtube_service.channels().list(
            part='snippet, statistics',
            id=user,
        )
        response = request.execute()
        print(json.dumps(response, indent=2))

        v1(response)

    except Exception as e:
        print(e)

call_yt()