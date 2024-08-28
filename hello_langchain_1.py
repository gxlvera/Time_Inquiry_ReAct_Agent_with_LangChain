from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model='gpt-3.5-turbo')

query="How is the University of Hong Kong"
messages = [
    SystemMessage(content="You are a helpful assistant.Limit your answer to 50 tokens"),
    HumanMessage(content=query)
]

result = llm.invoke(messages)

print(result)


