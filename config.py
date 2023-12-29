import os
from dotenv import load_dotenv
load_dotenv()

GPT_MODEL = os.environ.get('GPT_MODEL', 'gpt-4-1106-preview')
PSW = os.environ.get('PSW', '')
YOUTUBE_CHANNEL_ID = os.environ.get('YOUTUBE_CHANNEL_ID', 'UCRvqjQPSeaWn-uEx-w0XOIg')
SEARCH_URL = os.environ.get('SEARCH_URL', 'https://www.googleapis.com/youtube/v3/search')
SEARCH_MIN_TIMEDELTA = os.environ.get('SEARCH_MIN_TIMEDELTA', 30)
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
GROUP_CHAT_ID = os.environ.get('GROUP_CHAT_ID', 0)

