from django.shortcuts import render
from rest_framework.views import APIView
from .helpers.log_manager import create_log
from rest_framework.response import Response
from rest_framework import status
from .serializers import PrimaryAPISerializer
from .controllers import pre_processor
import json
from .models import Endpoint
from .helpers import log_manager
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.


class PrimaryAPIEndpoint(APIView):
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        
        if request.method == 'POST':
            serializer = PrimaryAPISerializer(data=request.data)
            if serializer.is_valid():
                # Process the valid data, e.g., parse the URL
                text_payload = serializer.validated_data.get('text_payload')
                file_uploaded = serializer.validated_data.get('file_uploaded')
                #Check that either a file or text is passed in
                if text_payload == None and file_uploaded == None:
                    error_dict = log_manager.error_builder("No payload or file recieved",serializer.data)
                    return JsonResponse(error_dict, status=status.HTTP_400_BAD_REQUEST)
                

                if pre_processor.validate_json(text_payload) == False and text_payload != None:
                    create_log("Invalid JSON Passed", status.HTTP_400_BAD_REQUEST)
                    error_dict = log_manager.error_builder("Invalid JSON Passed",serializer.data)
                    return JsonResponse(error_dict, status=status.HTTP_400_BAD_REQUEST)
                

                #First create a Django Object to Call
                request_object = serializer.create(serializer.validated_data)
                response = pre_processor.manage_request(request_object)

                #This is where the logic goes
                return JsonResponse(response)
            
            else:

                log_error = "Log Error "  + " Value : " + str(request.data)
                create_log(log_error, status.HTTP_400_BAD_REQUEST)
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            log_error = "Log Error "  + " POST Request Not Used : " + str(request.data)
            create_log(log_error, status.HTTP_400_BAD_REQUEST)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
