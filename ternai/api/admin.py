from django.contrib import admin
from api.models import Endpoint, APICall, AIModel, Prompt, ExternalCall, Log

class EndPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

class AIModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','price_per_1ktoken', 'context_window')

class ExternalCallAdmin(admin.ModelAdmin):
    list_display = ('id','endpoint','tern_user_id')

class PromptAdmin(admin.ModelAdmin):
    list_display = ('id','name','instructions')

# Register your models here.
admin.site.register(Endpoint, EndPointAdmin)
admin.site.register(APICall)
admin.site.register(AIModel,AIModelAdmin)
admin.site.register(Prompt, PromptAdmin)
admin.site.register(ExternalCall, ExternalCallAdmin)
admin.site.register(Log)


