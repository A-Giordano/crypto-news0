from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import YoutubeLoader
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import ChatPromptTemplate
from pytube import Channel

if __name__ == "__main__":
    load_dotenv()

    import scrapetube

    videos = scrapetube.get_channel("UCRvqjQPSeaWn-uEx-w0XOIg")
    last_video = next(videos)
    last_video_id = last_video['videoId']
    last_video_url = f"https://www.youtube.com/watch?v={last_video_id}"
    print(next(videos))
    previous_video = ""
    if last_video_url != previous_video:
        pass

    # c = Channel('https://www.youtube.com/@intothecryptoverse')
    #
    # print(c.video_urls[:3])

    gpt_model = "gpt-4-1106-preview"

    loader = YoutubeLoader.from_youtube_url(
        "https://www.youtube.com/watch?v=IlAiXeghgI8", add_video_info=True
    )
    transcript = loader.load()
    docs_n = len(transcript)
    docs_words = len(transcript[0].page_content)

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an expert in cryptocurrencies trading, able in generating relevant insights from youtube transcripts.
Your goal is to extract the author's sentiment and predictions on the market and an the various coins he talks about.
Finally, according to the transcript extract identifies BUY or SELL signals from the words of the author
Structure your output as:

Summary: [concise transcript summary, max 3 phrases]
Market sentiment: [author's market sentiment]
Market short-term prediction: [author's prediction on the short term evolution of the market]
Market long-term prediction: [author's prediction on the long term evolution of the market]
Short-term [coin] prediction: [author's prediction on the short term evolution of the discussed coin]
Long-term [coin] prediction: [author's prediction on the long term evolution of the discussed coin]
[coin] resistance levels: [resistance price levels]
[coin] support levels: [support price levels]
BUY/SELL signal: [[coin] - [BUY/SELL] - [price]]
"""),
        ("human", """Generate summary on this youtube transcript:

    {text}""")])

    # Define LLM chain
    llm = ChatOpenAI(temperature=0, model_name=gpt_model)
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Define StuffDocumentsChain
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

    print(stuff_chain.run(transcript))
    pass