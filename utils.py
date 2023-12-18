from langchain.chains import LLMChain, StuffDocumentsChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import YoutubeLoader
from langchain_core.prompts import ChatPromptTemplate
from prompts import system_message, human_message
from telegram import Bot
import config


def get_transcript(url):
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=False
                                            )
    return loader.load()


def get_summary(transcript):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", human_message)])
    print(f"key: {config.OPENAI_API_KEY[:5]}")

    # Define LLM chain
    llm = ChatOpenAI(temperature=0, model_name=config.GPT_MODEL, openai_api_key=config.OPENAI_API_KEY)
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    # Define StuffDocumentsChain
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

    return stuff_chain.run(transcript)


async def send_message(message):
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
