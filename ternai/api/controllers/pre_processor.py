from api.serializers import PrimaryAPISerializer
from api.models import ExternalCall
from api.models import Endpoints
from api.helpers import log_manager


#This manages the request 
def manage_request(PrimaryAPISerializer): 
    
    #First create a Django Object to Call
    request = PrimaryAPISerializer.create()
    
    #See if it's a valid 
    if is_endpoint_valid(request.id):
        #We know what endpoint to route this to
        text_to_parse = request.text_payload
        build_prompt(text_to_parse, request.id)
    else:
        log_manager.create_log("Invalid Endpoint ID Passed: " + str(PrimaryAPISerializer), "ERROR")


#A simple method to go through and find the Ids of the end point
def is_endpoint_valid(id_to_check:int): 
    all_endpoints = Endpoints.objects.all()
    ids = []

    for endpoint in all_endpoints: 
        ids.append(endpoint.id)

    if id_to_check in ids:
        return True
    else:
        return False

#This will build the actual prompt
def build_prompt(text_to_include:str, endpoint_id:int): 
    print('todo')


#This gets the actual details of the endpoint
def get_endpoint_by_id(endpoint_id:int): 
    print('todo')

