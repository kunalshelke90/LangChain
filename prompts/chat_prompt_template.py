from langchain_core.prompts import ChatPromptTemplate
"""
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

here we cannot use human message and system message like we did in prompt template

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]
"""

"""it is sued to create template just like prompt template but here is use for multi turn convesrational messages
and prompt template is for single turn messages"""


chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)