from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ParseURLSerializer
from .controllers import html_manager
from .controllers import ai_coordinator

class ParseURLView(APIView):
    def post(self, request, format=None):
        serializer = ParseURLSerializer(data=request.data)
        if serializer.is_valid():
            # Process the valid data, e.g., parse the URL
            
            model_values = serializer.data

            #TODO ADD ROUTING LOGIC HERE
            if model_values['run_type'] == 1:
                get_url = model_values['url_value']
                clean_html = html_manager.process_website(get_url)
                results = ai_coordinator.ai_parser(clean_html)

                
                return Response(results, status=status.HTTP_200_OK)
            else:
                return Response(results, status=status.HTTP_404_NOT_FOUND)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



