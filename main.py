from pm import PromptManager

CONTEXT = """
Q1: What is Devscale Indonesia?
A: Devscale Indonesia is a dedicated learning institution focused on equipping individuals with the practical skills and theoretical knowledge required to become proficient Software Engineers. We are committed to fostering the next generation of tech talent within Indonesia.

Q2: What is Devscale Indonesia's core mission?
A: Our mission is to bridge the tech talent gap in Indonesia by providing high-quality, accessible, and industry-relevant software engineering education. We aim to empower individuals from diverse backgrounds to build successful careers in technology and contribute to Indonesia's digital economy.
"""

pm = PromptManager()

while True:
	input_query = input("Query: ")
	pm.add_message("system", f'Answer the user query based on this text only:{CONTEXT}')
	pm.add_message("user", input_query)

	result = pm.generate()
	print(result)

	pm.add_message("assistant", result)
	