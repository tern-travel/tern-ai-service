from rest_framework import serializers
from .models import ExternalCall

#This handles the API View
class PrimaryAPISerializer(serializers.ModelSerializer):
    
    file_uploaded = serializers.FileField(required=False)  # Adjust required as per your need

    class Meta:
        model = ExternalCall
        fields = ['endpoint','text_payload','webhook_url','tern_user_id','file_uploaded']
        
    def create(self, validated_data):
        return ExternalCall.objects.create(**validated_data)