from dotenv import load_dotenv
import os

load_dotenv()

yt_api_key = os.environ.get('YT_API_KEY')
assert yt_api_key, "YT_API_KEY is not set in .env file."
print(f'init: ENV YT_API_KEY: {yt_api_key}')
