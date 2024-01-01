from django.db import models
import uuid

#This is a list of supported models and their API values. 
class AIModel(models.Model): 
    id = models.AutoField(primary_key=True)
    context_window = models.IntegerField()
    api_value = models.CharField(max_length=256, blank = False)
    name = models.CharField(max_length=256)
    price_per_1ktoken = models.DecimalField(max_digits=7, decimal_places=6)
    largest_token_model = models.BooleanField(default = False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.largest_token_model:
            # If this instance is set to be the largest_token_model,
            # set all others to not be the largest_token_model.
            AIModel.objects.filter(largest_token_model=True).update(largest_token_model=False)
        super(AIModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


#These are the prompts that help us construct the calls to openAI. e.g.gpt-3.5-turbo-0613
class Prompt(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique = True, blank=True)
    instructions = models.TextField(blank = False)
    example_response = models.TextField(blank = False)
    required_response_keys = models.JSONField(blank=True, null=True) #used to validate the model gives back the required values
    model = models.ForeignKey(AIModel, on_delete = models.RestrictedError)
    ai_temperature = models.IntegerField()

    def __str__(self):
        return self.name

# This is used to route to the right endpoint
class Endpoint(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique = True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=30, unique = True)
    prompt = models.ForeignKey(Prompt, on_delete = models.RestrictedError)
    description = models.TextField()

    def __str__(self):
        return self.name + " : "  + self.prompt.model.name


#This takes in the JSON Object
class ExternalCall(models.Model): 
    id = models.AutoField(primary_key=True)
    endpoint = models.ForeignKey(Endpoint, on_delete = models.DO_NOTHING)
    webhook_url = models.URLField()
    text_payload = models.TextField(blank=True, null=True)
    description = models.TextField()
    tern_user_id = models.IntegerField()
    file_uploaded = models.FileField(upload_to='pdfs/', blank=True, null=True)

class Log(models.Model): 
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    type = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #This is the table that actually tracks the calls we're making and their results/status.
class APICall(models.Model): 
    id = models.AutoField(primary_key=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prompt_text = models.TextField()
    in_progress = models.BooleanField()
    complete = models.BooleanField()
    response = models.JSONField(blank = True)
    source_call = models.ForeignKey(ExternalCall, on_delete=models.RESTRICT, blank = True)
    error_text = models.TextField()
    valid_resopnse = models.BooleanField()


    def __str__(self):
        return self.source_call.endpoint.name + " User: " + str(self.source_call.tern_user_id)
    

