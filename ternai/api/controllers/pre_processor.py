from api.serializers import PrimaryAPISerializer
from django.http import HttpResponseBadRequest
import json
from api.models import ExternalCall, Endpoint, Prompt 
from api.helpers import log_manager, pdf_manager
from api.controllers import ai_caller
import tiktoken


#A super simple method to validate JSON
def validate_json(text_given:str):
    try: 
        json.loads(text_given)
        return True
    except:
        return False

#This manages the request 
def manage_request(created_object:ExternalCall): 
    
    #See if it's a valid 
    if is_endpoint_valid(created_object.endpoint_id):
        #We know what endpoint to route this to
        text_to_parse = ""
        content_dict = {}

        if created_object.text_payload != None:
            content_dict = json.loads(created_object.text_payload)

        if created_object.file_uploaded != None:
            file_dict = {}
            file_text = pdf_manager.extract_text(created_object.file_uploaded.path)
            created_object.file_uploaded.name
            file_dict['content'] = file_text
            content_dict = content_dict | file_dict


        prompt = build_prompt(content_dict, created_object.endpoint_id)
        force_max = check_prompt_and_model_compatability(created_object.endpoint_id, prompt)
        response = ai_caller.make_ai_call(prompt, created_object,force_max)

        return response
        
    else:
        log_manager.create_log("Invalid Endpoint ID Passed: " + str(PrimaryAPISerializer), "ERROR")

#A simple method to go through and find the Ids of the end point
def is_endpoint_valid(id_to_check:int): 
    all_endpoints = Endpoint.objects.all()
    ids = []

    for endpoint in all_endpoints: 
        ids.append(endpoint.id)

    if id_to_check in ids:
        return True
    else:
        return False

#This will build the actual prompt
def build_prompt(text_dict:dict, endpoint_id:int): 
    
    endpoint = get_endpoint_by_id(endpoint_id)
    prompt = endpoint.prompt
    prompt_text = ""

    text_to_consider = ""
    #we're going to iterate through all the keys and smush it into one text blob
    for key in text_dict:
        text_to_consider = text_to_consider + str(key) + ": " + str(text_dict[key])

    prompt_text = prompt_text + "<TEXT START> " + text_to_consider + " <TEXT END>"
    prompt_text = prompt_text + "<SAMPLE START> " + prompt.example_response + "<SAMPLE END> "

    return prompt_text

#This gets the actual details of the endpoint
def get_endpoint_by_id(endpoint_id:int): 
    return Endpoint.objects.get(id=endpoint_id)

#This checks if the model and the tokens will work or if we should use the fallback.
def check_prompt_and_model_compatability(endpoint_id:int, prompt:str):
    
    endpoint_used = get_endpoint_by_id(endpoint_id)
    token_requirement = calculate_token_count(prompt, endpoint_used.prompt.model.api_value) + 4000 #Assume we're using close to the max number of tokens for the response. Room to make this smarter over time.
    possible_tokens = endpoint_used.prompt.model.context_window

    if possible_tokens <= token_requirement:
        return True
    else:
        return False

#Calculates the number of tokens a message will take
def calculate_token_count(prompt:str, model_name:str): 
    
    encoding = tiktoken.encoding_for_model(model_name)
    token_array = encoding.encode(prompt)
    token_estimate = len(token_array)

    return token_estimate