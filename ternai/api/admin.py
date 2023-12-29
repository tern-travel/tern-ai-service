from django.contrib import admin
from api.models import Endpoint, APICall, AIModel, Prompt, ExternalCall, Log

# Register your models here.
admin.site.register(Endpoint)
admin.site.register(APICall)
admin.site.register(AIModel)
admin.site.register(Prompt)
admin.site.register(ExternalCall)
admin.site.register(Log)
