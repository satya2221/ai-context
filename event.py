from pm import PromptManager
from pydantic import BaseModel, Field

class AnalyzeEvent(BaseModel):
    is_event: bool = Field(description="Information of the query if contain an event") # memberikan informasi yang lebih tepat mengenai skema kita
    description: str = Field(description="Description of event")
    confident_score: float = Field(description="How confidence you are between 0 to 1")

def run():
    pm = PromptManager()
    pm.add_message("user", "I'd like to have meeting with Julia at Wednesday 2pm")

    result = pm.generate_structure(AnalyzeEvent)
    print(result)

if __name__ == "__main__":
    run()