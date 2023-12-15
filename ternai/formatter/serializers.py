from rest_framework import serializers
from formatter.models import URLtoParse

class ParseURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLtoParse
        fields = '__all__'