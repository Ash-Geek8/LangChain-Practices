import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

os.environ["GOOGLE_API_KEY"] = "AQ.Ab8RN6Ihu9stTz0gB7QUJHp4ysgEyOucK8uL5zCrlbcrRQPRvA"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

prompt = PromptTemplate.from_template(
    "Give me a recipe to make {dish} for {ppl} people."
)

chain = prompt | llm

response = chain.invoke(
    {
        "dish": "Egg Gravy",
        "ppl": "1"
    }
)

print(response.content)