from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from . import models

class LotSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    gallery = serializers.CharField(required=True)
    
    lot_type = serializers.CharField(required=True)
    bedrooms = serializers.CharField(required=True)
    bathrooms = serializers.CharField(required=True)
    sims = serializers.CharField(required=True)
    
    images = serializers.CharField(required=True)
    
    author_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return models.Lot.objects.create(**validated_data)
    
    def partial_update(self, instance, validated_data):
        print(instance.name)
        print(validated_data)
        print(validated_data.get('name'))
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.gallery = validated_data.get('gallery', instance.gallery)

        instance.lot_type = validated_data.get('lot_type', instance.lot_type)
        instance.bedrooms = validated_data.get('bedrooms', instance.bedrooms)
        instance.bathrooms = validated_data.get('bathrooms', instance.bathrooms)
        instance.sims = validated_data.get('sims', instance.sims)

        instance.images = validated_data.get('images', instance.images)

        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance

    class Meta:
        # fields = (
        #     'name',
        #     'description',
        #     'gallery',
        #     'lot_type',
        #     'bedrooms',
        #     'bathrooms',
        #     'sims',
        #     'images',
        #     'author'
        #     )
        fields = '__all__'
        model = models.Lot
            