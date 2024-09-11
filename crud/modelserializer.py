from rest_framework import serializers
from .models import *

class AnimeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200, required=True)
    character = serializers.CharField(max_length=200, required=True)
    role = serializers.CharField(max_length=200, required=True)


    def create(self, validated_data):  

        return Anime.objects.create(**validated_data)  
    
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id',instance.id)
        instance.name = validated_data.get('name',instance.name)
        instance.character = validated_data.get('character',instance.character)
        instance.role = validated_data.get('role',instance.role)

        instance.save()
        return instance