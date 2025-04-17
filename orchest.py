# Generate Blog

## prompt nya chatgpt untuk blok sebagian besar akan seperti ini
## "Write a blog about LLM for daily task"
## Hasilnya biasanya akan panjang tapi kualitasnya dipertanyakan
## Orchest akan memecah prompt ini menjadi bagian-bagian kecil
## Setiap chunknya akan diiterasi

## Nah Better watnya
## - Generate Title (1st step)
## - Generate Section (1st step)
## - Write content for each section (Melanjutkan dari section yang ada)
## - Re-check the cohesion beteween section (Pengecekan dari konten setiap bagiannya)

from pm import PromptManager
from prompt import GENERATE_TITLE_PROMPT, GENERATE_SECTION_PROMPT, GENERATE_TITLE_PROMPT

class GenerateBlog:
    def __init__(self, topic):
        self.topic= topic
        self.section = {}

    def generate_title(self):
        pm = PromptManager()
        pm.add_message("system", GENERATE_TITLE_PROMPT.format(topic= self.topic))
        pm.add_message("user", "Generate a title for blog content")

        return pm.generate()
    
    def generate_section(self):
        pm = PromptManager()
        pm.add_message("system", GENERATE_SECTION_PROMPT.format(topic= self.topic))
        pm.add_message("user", "Generate the blog section!")

        return pm.generate()

    def generate_content(self, section_title):
        pm = PromptManager()
        pm.add_message("system", GENERATE_TITLE_PROMPT.format(section_title= section_title))
        pm.add_message("user", "Generate the content based on the section title!")

        return pm.generate()

def generate_blog():
    client = GenerateBlog(topic="Why Learning python is important for developer?")

    title = client.generate_title()
    sections = client.generate_section()

    print(f"Title = {title}")
    print(f"Section : {sections} ")

if __name__ == "__main__":
    generate_blog()