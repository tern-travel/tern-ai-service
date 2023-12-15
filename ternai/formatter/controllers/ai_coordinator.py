import openai
import json
from openai import OpenAI
OPENAI_API_KEY= "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"


#Structruing the text with AI
def ai_parser(clean_text:str): 


    prompt_prefix = load_prompt_from_file('ternai/formatter/prompts/structure_text.txt')
    client = OpenAI()

    chat_messages = [
        {"role": "system","content": prompt_prefix},{"role": "user","content": clean_text} 
    ]

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        temperature=0.1,
        max_tokens=4095,
        top_p=.5,
        frequency_penalty=0,
        presence_penalty=0,
        messages = chat_messages
    )

    response = response.choices[0].message.content

    response = response.replace('`',"")    
    response = response.replace('\n'," ")    

    iterate_through_parsed_objects(response)

    return response


def iterate_through_parsed_objects(objects_to_parse:str):
    print('todo')

    events = json.load(objects_to_parse) 

    for itinerary_item in events:
        detailed_activity(itinerary_item[''])

    
def detailed_activity(content:str, type:str, day:str): 

    prompt_file_path = ""
    
    if type == "lodging": 
        prompt_file_path = "TODO"

    elif type == "flight":
        prompt_file_path = "TODO"

    elif type == "transfer":
        prompt_file_path = "TODO"

    elif type == "activity": 
        prompt_file_path = "TODO"

    elif type == "information":
        prompt_file_path = "TODO"


    core_prompt = load_prompt_from_file(prompt_file_path)
    client = OpenAI()

    chat_messages = [
        {"role": "system","content": core_prompt},{"role": "user","content": content} 
    ]

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        temperature=0.1,
        max_tokens=4095,
        top_p=.5,
        frequency_penalty=0,
        presence_penalty=0,
        messages = chat_messages
    )

    response = response.choices[0].message.content


#breaks out the parsing 
def load_prompt_from_file(filepath:str):
    core_prompt_file = open(filepath, 'r')
    core_prompt = core_prompt_file.read()
    return core_prompt
