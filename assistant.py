from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from langchain.tools import Tool
from langchain.utilities.bing_search import BingSearchAPIWrapper
from langchain.agents import AgentExecutor
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.llms import OpenAI
from langchain.utilities.zapier import ZapierNLAWrapper
from langchain.agents import AgentType, initialize_agent

def init_assistant():

    ##########################################
    llm = OpenAI(temperature=0)
    zapier = ZapierNLAWrapper()
    toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)

    search = BingSearchAPIWrapper()
    # search = DuckDuckGoSearchRun()
    # search = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    # search = GoogleSearchAPIWrapper()

    search_tool = Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about the current state of the world. You should ask targeted questions"
    )

    tools = [search_tool].extend(toolkit.get_tools())

    agent = OpenAIAssistantRunnable.create_assistant(
        name="langchain test assistant",
        instructions="You are a personal math tutor. Write and run code to answer math questions. You can also search the internet.",
        tools=tools,
        # model="gpt-4-1106-preview",
        model="gpt-3.5-turbo-1106",
        as_agent=True,
    )
    return AgentExecutor(agent=agent, tools=tools)



def chat_assistant(assistant):
    assistant.invoke({"content": "What's the weather in SF today divided by 2.7"})