from django.contrib import admin
from formatter.models import Endpoints, ActivityTypes, ParsingLog, SupportedContentTypes


# Register your models here.
admin.site.register(Endpoints)
admin.site.register(ActivityTypes)
admin.site.register(ParsingLog)
admin.site.register(SupportedContentTypes)
