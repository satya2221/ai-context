from pm import PromptManager
from pydantic import BaseModel, Field
from datetime import datetime
import json

class AnalyzeEvent(BaseModel):
    is_event: bool = Field(description="Information of the query if contain an event") # memberikan informasi yang lebih tepat mengenai skema kita
    description: str = Field(description="Description of event")
    confident_score: float = Field(description="How confidence you are between 0 to 1")

class EventDetail(BaseModel):
    name: str = Field(description="The name of the event")
    description: str = Field(description="The description of the event")
    datetime: str = Field(description="Date time of the event")
    duration: str = Field(description="Duration of the event")

def analyze_event(query):
    pm = PromptManager()
    pm.add_message("user", query)

    result = pm.generate_structure(AnalyzeEvent)
    is_event = result.get("is_event")
    description = result.get("description")
    confidence_score = result.get("confident_score")

    return is_event, description, confidence_score

def extract_event(query):
    today = datetime.today()
    formatted_date = today.strftime("%Y-%m-%d")
    pm = PromptManager()
    pm.add_message("system", f"Extract event details based on user query, as additional information today date is {formatted_date}")
    pm.add_message("user", query)

    result = pm.generate_structure(EventDetail)
    return result

def aggregate_event(current_event:str, new_event:str):
    pm = PromptManager()
    pm.add_message("system", f"You have list of user current events, and check if its already exist. Here is the event:{current_event}")
    pm.add_message("user", new_event)

    result = pm.generate()
    return result

def get_current_event():
    return """
    Event List:

    - name: Meeting with product team
      date: 17 april 2025, 1.00 PM
      duration : 2 hour
    
    - name: Meeting with investor
      date: 19 April 2025, 10.00 AM
      duration: 1.5 hour
    """

def generate_confirmation(query):
    pm = PromptManager()
    pm.add_message("system", 
                   """
                    Create a confirmation message to the user, and ask if it's confirmed.

                    EXAMPLE RESPONSE OUTPUT:
                    Hey, I will make an event for you with this detail: follow with the event details.
                    Let me know if it's good!
                   """)
    pm.add_message("user", query)
    
    return pm.generate()

def run():
    input_query = input("Query: ")
    is_event, description, confidence_score = analyze_event(input_query)
    
    if is_event and confidence_score > 0.7:
        current_event = get_current_event()
        new_event = extract_event(description)

        agg_result = aggregate_event(current_event, json.dumps(new_event))

        print(agg_result)

        # result = generate_confirmation(json.dumps(event))

        # print(result)
    else:
        print("Not Event")

if __name__ == "__main__":
    run()