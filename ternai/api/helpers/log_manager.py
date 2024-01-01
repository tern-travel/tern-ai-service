from api.models import Log

#Creates 
def create_log(log_text:str, log_type:str): 
    print('log created')
    new_log = Log(message=log_text,type = log_type)
    new_log.save()

# a simple function to manage building a dictionary with error information
def error_builder(error_text:str, dict_data:dict): 
    error_dict = {}
    error_dict['error'] = error_text
    error_dict['input'] = dict_data
    return error_dict