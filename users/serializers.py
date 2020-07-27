from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group

class MyGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name')

class MyUserSerializer(serializers.ModelSerializer):
    all_groups = MyGroupSerializer(source='groups', many=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'all_groups')


class MyTokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source="key")
    
    class Meta:
        model = Token
        fields = ("auth_token",)

