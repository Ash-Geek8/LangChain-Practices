import os
os.environ["GOOGLE_API_KEY"] = "AQ.Ab8RN6Ihu9stTz0gB7QUJHp4ysgEyOucK8uL5zCrlbcrRQPRvA"

import base64
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages.human import HumanMessage
with open("test.jpg", 'rb') as image_file:
    image_bytes = image_file.read()
    base64_bytes = base64.b64encode(image_bytes).decode("utf-8")
prompt = [
   {"type": "text", "text": "Describe the image: "},
   {"type": "image_url", "image_url": {"url": f"data:image/jpg;base64,{base64_bytes}"}},
]
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)
response = llm.invoke([HumanMessage(content=prompt)])
print(response.content)