import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

class PromptManager:
    def __init__(self, messages = [], model='gpt-4o-mini'):
        self.messages = messages
        self.model = model
    
    def add_message(self, role, content):
        self.messages.append(
            {"role": role, "content": content}
        )
    
    def generate(self):
        response = client.chat.completions.create(
            model=self.model, messages=self.messages 
        )
        return response.choices[0].message.content
    
    def generate_structure(self, schema):
        response = client.beta.chat.completions.parse(
            model=self.model,
            messages=self.messages,
            response_format=schema
        )
        result = response.choices[0].message.model_dump()
        return result