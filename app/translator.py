from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="ggml-model-q5-k-m:latest")

translator_prompt = ChatPromptTemplate.from_template(
    "Translate following sentence in Korean:\\n{input}"
)

EN_TO_KO_CHAIN = translator_prompt | llm | StrOutputParser()