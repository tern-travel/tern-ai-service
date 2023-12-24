from rest_framework import serializers
from .models import ExternalCall

#This handles the API View
class PrimaryAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalCall
        fields = ['endpoint_id','json_payload','webhook_url']
        
        def create(self, validated_data):
            return ExternalCall.objects.create(**validated_data)