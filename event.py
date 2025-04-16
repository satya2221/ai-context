from pm import PromptManager
from pydantic import BaseModel, Field
from datetime import date

class AnalyzeEvent(BaseModel):
    is_event: bool = Field(description="Information of the query if contain an event") # memberikan informasi yang lebih tepat mengenai skema kita
    description: str = Field(description="Description of event")
    confident_score: float = Field(description="How confidence you are between 0 to 1")

class EventDetail(BaseModel):
    name: str = Field(description="The name of the event")
    description: str = Field(description="The description of the event")
    datetime: str = Field(description="Date time of the event")
    duration: str = Field(description="Duration of the event")

def analyze_event():
    pm = PromptManager()
    pm.add_message("user", "I'd like to have meeting with Julia at Wednesday 2pm")

    result = pm.generate_structure(AnalyzeEvent)
    is_event = result.get("is_event")
    description = result.get("description")
    confidence_score = result.get("confident_score")

    return is_event, description, confidence_score

def extract_event(query):
    today = date.today()
    pm = PromptManager()
    pm.add_message("system", f"Extract event details based on user query, as additional information today date is {today}")
    pm.add_message("user", query)

    result = pm.generate_structure(EventDetail)
    print(result)

def run():
    is_event, description, confidence_score = analyze_event()
    
    if is_event and confidence_score > 0.7:
        extract_event(description)
    else:
        print("Not Event")

if __name__ == "__main__":
    run()