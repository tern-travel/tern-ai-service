from django.db import models

# Create your models here.

class Endpoints(models.Model): 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name  = models.CharField(max_length=256) #
    slug = models.CharField(max_length=30) #the URL we use to route it
    core_prompt = models.TextField() #this is the core prompt that we send to OpenAI
    archived = models.BooleanField()
    
    def __str__(self):
        return self.name

#This is the type of content we support
class SupportedContentTypes(models.Model):
    name = models.CharField(max_length=256)
    descriptions = models.TextField()
    
    def __str__(self):
        return self.name

    
#We use this to validate the JSON we get
class URLtoParse(models.Model):
    url_value = models.URLField()
    run_type = models.ForeignKey(SupportedContentTypes, on_delete=models.RESTRICT) #don't


#We need to model the Tern activities 
class ActivityTypes(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=256)
    type_tern_id = models.IntegerField()
    sample_json = models.JSONField() #this is what we give to OpenAi to handle the parsing

    def __str__(self):
        return self.type


#We want to keep track of the logs so we can debug them 
class ParsingLog(models.Model): 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url_passed = models.URLField()
    prompt_generated = models.TextField()
    result = models.JSONField()
    endpoint = models.ForeignKey(Endpoints, on_delete=models.RESTRICT) #don't

    def __str__(self):
        return self.url_passed