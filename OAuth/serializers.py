from django.urls import path, include
from OAuth.models import (newuser, Ship, ShipCrew)
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = newuser
        fields = ['url', 'username', 'email', 'is_staff', 'id', 'typevalue', 'roles']

class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = '__all__'

class ShipCrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipCrew
        # fields = ['ShipID', 'user']
        fields = '__all__'

class ShipCrewSerializer2(serializers.ModelSerializer):
    class Meta:
        model = newuser
        # fields = ['ShipID', 'user']
        fields = '__all__'
    def create(self, validated_data):
        user_info_data = validated_data.pop('ShipID')
        user = newuser.objects.create(**validated_data)
        ShipCrew.objects.create(user=user, **user_info_data)
        return user