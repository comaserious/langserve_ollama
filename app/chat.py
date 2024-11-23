from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


llm = ChatOllama(model="ggml-model-q5-k-m:latest")

chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI Assistant. Your name is '자비스'. You munst answer in Korean."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chat_chain = chat_prompt | llm | StrOutputParser()
