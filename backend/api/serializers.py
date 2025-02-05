from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer) :
    class Meta:
        model = CustomUser
        fields = ["id","username","email","pfp","bio","first_name", "last_name","verified"]
    
    def get_image(self, obj):
        if obj.image:
            return obj.image.name  # This ensures the relative path is returned
        return None