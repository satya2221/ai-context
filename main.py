import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

CONTEXT = """
Q1: What is Devscale Indonesia?
A: Devscale Indonesia is a dedicated learning institution focused on equipping individuals with the practical skills and theoretical knowledge required to become proficient Software Engineers. We are committed to fostering the next generation of tech talent within Indonesia.

Q2: What is Devscale Indonesia's core mission?
A: Our mission is to bridge the tech talent gap in Indonesia by providing high-quality, accessible, and industry-relevant software engineering education. We aim to empower individuals from diverse backgrounds to build successful careers in technology and contribute to Indonesia's digital economy.
"""


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

messages = [
	{'role':'system', 'content': f'Answer the user query based on this text only:{CONTEXT}'},
]

while True:
	input_query = input("Query: ")
	messages.append({'role':'user', 'content': input_query})
	
	response = client.chat.completions.create(
    model="gpt-4o-mini", messages=messages 
	)
	content = response.choices[0].message.content
	
	print(content)
	print("--------")
	messages.append({'role': 'assistant', 'content': content})
	
	print(messages)
	print("--------")