"""
This script employs chain and prompt template of LangChain to query chatGPT
"""

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(model='gpt-3.5-turbo')

query="ATEEZ"
prompt_template = PromptTemplate.from_template("who is {input}? Answer with < 30 tokens")

output_parser=StrOutputParser()
chain=prompt_template | llm | output_parser
result = chain.invoke({"input":query}) 

print(result)


