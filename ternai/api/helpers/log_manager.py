from api.models import Log

#Creates 
def create_log(log_text:str, log_type:str): 
    print('log created')
    new_log = Log(message=log_text,type = log_type)
    new_log.save()