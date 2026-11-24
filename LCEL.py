from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = "AQ.Ab8RN6Ihu9stTz0gB7QUJHp4ysgEyOucK8uL5zCrlbcrRQPRvA"

prompt = PromptTemplate.from_template("Tell me a joke about {topic}")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)
output_parser = StrOutputParser()


# Chain them together using LCEL
chain = prompt | llm | output_parser
#  Execute the workflow with a single call
result = chain.invoke({"topic": "programming"})
print(result)