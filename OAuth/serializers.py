from django.urls import path, include
from OAuth.models import newuser
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = newuser
        fields = ['url', 'username', 'email', 'is_staff']