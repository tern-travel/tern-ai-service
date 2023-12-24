from django.db import models
import uuid


#This is the table that actually tracks the calls we're making and their results/status.
class APICall(models.Model): 
    id = models.AutoField(primary_key=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prompt_text = models.TextField()
    in_progress = models.BooleanField()
    complete = models.BooleanField()
    response = models.TextField()

#This is a list of supported models and their API values. 
class AIModel(models.Model): 
    id = models.AutoField(primary_key=True)
    context_window = models.IntegerField()
    api_value = models.CharField(max_length=256, blank = False)
    name = models.CharField(max_length=256)


#These are the prompts that help us construct the calls to openAI. e.g.gpt-3.5-turbo-0613
class Prompt(models.Model): 
    id = models.AutoField(primary_key=True)
    instructions = models.TextField(blank = False)
    ai_model = models.CharField(max_length = 256, help_text = "The OpenAI Model to Use (e.g.gpt-3.5-turbo-0613)")
    example_response = models.TextField(blank = False)
    model = models.ForeignKey(AIModel, on_delete = models.RestrictedError)


# This is used to route to the right endpoint
class Endpoints(models.Model): 
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=30, unique = True)
    prompt = models.ForeignKey(Prompt, on_delete = models.RestrictedError)


#This takes in the JSON Object
class ExternalCall(models.Model): 
    id = models.AutoField(primary_key=True)
    endpoint_id = models.ForeignKey(Endpoints, on_delete = models.DO_NOTHING)
    webhook_url = models.URLField()
    text_payload = models.TextField()


class Log(models.Model): 
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    type = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)