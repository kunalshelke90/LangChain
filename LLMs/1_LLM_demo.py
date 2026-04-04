from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

response = llm.invoke("Explain transformers in simple terms")
print(response)