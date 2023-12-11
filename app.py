import os
from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl

import uuid
import time
import os

# @cl.langchain_factory(use_async=False)
# def factory():
#     # prompt = PromptTemplate(template=template, input_variables=["question"])
#     # llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)
#
#     return get_agent(namespace=str(uuid.uuid4()))
from assistant import init_assistant


@cl.on_chat_start
def init():
    s = time.time()
    print(f"PINECONE_API_KEY {os.getenv('PINECONE_API_KEY')}")
    chain = init_assistant()
    print(f"exec time: {time.time() - s}")
    cl.user_session.set("chain", chain)
    # await cl.Message(content=welcome_message()).send()


@cl.on_message
async def main(message):
    chain = cl.user_session.get("chain")
    print(f"PINECONE_API_KEY {os.getenv('PINECONE_API_KEY')}")
    print(message.content)
    res = chain.invoke({"content": message.content})
    print(res)
    await cl.Message(content=res).send()
