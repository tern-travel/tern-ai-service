from django.urls import path
from .views import ParseURLView

urlpatterns = [
    path('api/parse_url', ParseURLView.as_view(), name='parse_url')
]