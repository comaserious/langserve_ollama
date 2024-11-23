from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="ggml-model-q5-k-m:latest")

prompt = ChatPromptTemplate.from_template("{topic} 에 대하여 간략히 설명해줘.")

chain = prompt | llm | StrOutputParser()



