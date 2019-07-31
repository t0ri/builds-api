from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from . import models

class LotSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    gallery = serializers.CharField(required=True)

    lot_type = serializers.CharField(required=True)
    bedrooms = serializers.CharField(required=True)
    bathrooms = serializers.CharField(required=True)
    sims = serializers.CharField(required=True)

    packs = serializers.CharField(required=True)


    # def create(self, validated_data):
    #     user = User.objects.create_user(validated_data['username'], validated_data['email'],
    #          validated_data['password'])
    #     return user

    class Meta:
        model = models.Lot
        fields = '__all__'
