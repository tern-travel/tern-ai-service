from api.serializers import PrimaryAPISerializer
import json
from api.models import ExternalCall
from api.models import Endpoint
from api.helpers import log_manager
from api.controllers import ai_caller


#This manages the request 
def manage_request(created_object:ExternalCall): 
    
    #See if it's a valid 
    if is_endpoint_valid(created_object.endpoint_id):
        #We know what endpoint to route this to
        text_to_parse = created_object.text_payload
        prompt = build_prompt(text_to_parse, created_object.endpoint_id)
        response = ai_caller.make_ai_call(prompt, created_object)
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
def build_prompt(text_to_include:str, endpoint_id:int): 
    
    endpoint = get_endpoint_by_id(endpoint_id)
    prompt = endpoint.prompt
    prompt_text = ""

    text_dict = json.loads(text_to_include)

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

