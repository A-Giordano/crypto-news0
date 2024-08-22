import datetime
from langchain.chains import LLMChain, StuffDocumentsChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import YoutubeLoader
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.prompts import ChatPromptTemplate
from prompts import system_message, human_message
from telegram import Bot
import config
import requests
import asyncio


def get_new_video_id(timedelta):
    current_time = datetime.datetime.utcnow()
    time_window = current_time - datetime.timedelta(minutes=timedelta)
    # time_window = current_time - datetime.timedelta(days=1)
    # Convert the time window to RFC 3339 format
    time_window_str = time_window.isoformat("T") + "Z"
    # Parameters for the API request
    params = {
        'part': 'snippet',
        'channelId': config.YOUTUBE_CHANNEL_ID,
        'type': 'video',
        'order': 'date',  # Order by the latest videos
        'publishedAfter': time_window_str,  # Only get videos after the time window
        'key': config.YOUTUBE_API_KEY,
    }

    # Make the API request
    response = requests.get(config.SEARCH_URL, params=params)
    videos = response.json().get('items', [])
    video_ids = [video['id']['videoId'] for video in videos]
    print(f"video_ids: {video_ids}")
    return video_ids


def get_transcript(url):
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=False, language=['en', 'it'])
    return loader.load()


def get_transcript_2(video_url):
    # Extract the video ID from the URL
    video_id = video_url.split("?v=")[1]

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id,
                                                         proxies={"socks5": f"socks5://{config.PROXY_USER}:{config.PROXY_PSW}@{config.PROXY_DOMAIN}:{config.PROXY_PORT}"})
        return " ".join([entry["text"] for entry in transcript])
    except Exception as e:
        print(f"Error: {e}")
        return ""


def get_summary(transcript):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", human_message)])
    # print(f"key: {config.OPENAI_API_KEY[:5]}")

    # Define LLM chain
    llm = ChatOpenAI(temperature=0, model_name=config.GPT_MODEL, openai_api_key=config.OPENAI_API_KEY)
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    # Define StuffDocumentsChain
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

    return stuff_chain.run(transcript)


def get_summary_2(transcript):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", human_message)])
    # print(f"key: {config.OPENAI_API_KEY[:5]}")

    # Define LLM chain
    llm = ChatOpenAI(temperature=0, model_name=config.GPT_MODEL, openai_api_key=config.OPENAI_API_KEY)

    chain = prompt | llm

    return chain.invoke({"text": transcript}).content


def send_message(message):
    # Initialize the bot
    bot = Bot(token=config.BOT_TOKEN)
    # Send a message to the group chat
    asyncio.run(bot.send_message(chat_id=config.GROUP_CHAT_ID, text=message))
    print("Message sent!")


async def async_send_message(message):
    # Initialize the bot
    bot = Bot(token=config.BOT_TOKEN)
    # Send a message to the group chat
    await bot.send_message(chat_id=config.GROUP_CHAT_ID, text=message)
    print("Message sent!")


async def psw_correct(psw):
    print(f"-{psw}-")
    print(f"-{type(psw)}-")
    print(f"o-{config.PSW}-")
    print(f"o-{type(config.PSW)}-")
    test = psw.strip() == config.PSW
    print(f"test {test}")
    return psw.strip() == config.PSW
