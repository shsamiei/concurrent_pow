from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


# User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):

#     class Meta :
#         model = User
#         fields = ['username', 'password']

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', 'password']