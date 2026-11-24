import os
from langchain_google_genai import ChatGoogleGenerativeAI
os.environ["GOOGLE_API_KEY"] = "AQ.Ab8RN6Ihu9stTz0gB7QUJHp4ysgEyOucK8uL5zCrlbcrRQPRvA"
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=1)
response = llm.invoke("Tell me a joke about light bulbs!")
print(response.content)