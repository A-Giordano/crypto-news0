import os
from dotenv import load_dotenv
load_dotenv()

GPT_MODEL = os.environ.get('GPT_MODEL', 'gpt-4-1106-preview')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
GROUP_CHAT_ID = os.environ.get('GROUP_CHAT_ID', 0)
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
