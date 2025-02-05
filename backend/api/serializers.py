from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer) :
    class Meta:
        model = CustomUser
        fields = ["id","username","email","first_name", "last_name"]
    
    # def get_image(self, obj):
    #     if obj.image:
    #         return obj.image.name  # This ensures the relative path is returned
    #     return None

class DocumentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Document
        fields = ['uid', 'fileName', 'cid', 'createdat', 'user']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['uid', 'title', 'content', 'created_at', 'document']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['uid', 'senderIsUser', 'content', 'document', 'created_at']
