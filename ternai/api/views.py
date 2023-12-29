from django.shortcuts import render
from rest_framework.views import APIView
from .helpers.log_manager import create_log
from rest_framework.response import Response
from rest_framework import status
from .serializers import PrimaryAPISerializer
from .controllers import pre_processor
from .models import Endpoint
from django.http import JsonResponse

# Create your views here.


class PrimaryAPIEndpoint(APIView):
    
    def post(self, request, format=None):
        
        if request.method == 'POST':
            serializer = PrimaryAPISerializer(data=request.data)
            if serializer.is_valid():
                # Process the valid data, e.g., parse the URL

                #First create a Django Object to Call
                request_object = serializer.create(serializer.validated_data)
                response = pre_processor.manage_request(request_object)

                #This is where the logic goes
                return JsonResponse(response)
            
            else:

                log_error = "Log Error "  + " Value : " + str(request.data)
                create_log(log_error, status.HTTP_400_BAD_REQUEST)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            log_error = "Log Error "  + " POST Request Not Used : " + str(request.data)
            create_log(log_error, status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
