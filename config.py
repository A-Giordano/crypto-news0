import os
# from dotenv import load_dotenv
# load_dotenv()

GPT_MODEL = os.getenv('GPT_MODEL', 'gpt-4-1106-preview')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')
GROUP_CHAT_ID = os.getenv('GROUP_CHAT_ID', 0)
