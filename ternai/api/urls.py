from django.urls import path
from .views import PrimaryAPIEndpoint

urlpatterns = [
    path('ai', PrimaryAPIEndpoint.as_view(), name='api_endpoint')
]
