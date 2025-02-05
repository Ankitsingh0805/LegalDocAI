from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

from django.contrib.auth import authenticate

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields=['email', 'username', 'password', 'password2', 'pfp','first_name','last_name', 'bio']
        extra_kwargs={
        'password':{'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        if len(password) < 8 :
            raise serializers.ValidationError("Password is too short")
        
        return attrs


    def create(self, validated_data):
        validated_data.pop('password2', None)
        instance = self.Meta.model.objects.create_user(**validated_data)
        return instance
