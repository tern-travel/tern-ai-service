from django.shortcuts import render
from rest_framework.views import APIView
from .helpers.log_manager import create_log
from rest_framework.response import Response
from rest_framework import status
from .serializers import PrimaryAPISerializer
from .controllers import pre_processor

# Create your views here.


class PrimaryAPIEndpoint(APIView):
    
    def post(self, request, format=None):
        
        if request.method == 'POST':
            serializer = PrimaryAPISerializer(data=request.data)
            if serializer.is_valid():
                # Process the valid data, e.g., parse the URL
                response = pre_processor(serializer)

                #This is where the logic goes
                return Response("results", status=status.HTTP_200_OK)
            
            else:

                log_error = "Log Error "  + " Value : " + str(request.data)
                create_log(log_error, status.HTTP_400_BAD_REQUEST)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            log_error = "Log Error "  + " POST Request Not Used : " + str(request.data)
            create_log(log_error, status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
