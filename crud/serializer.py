from rest_framework import serializers
from .models import Anime

# class AnimeSerializer(serializers.Serializer):
#     id = serializers.IntegerField(label='enter anime id ')
#     name = serializers.CharField(label='enter anime name')
#     character = serializers.CharField(label='enter main character')
#     role = serializers.CharField(label='enter role of charcter')

#     class Meta:
#         model =Anime
#         fields = '__all__'

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = "__all__"
        # fields = ['id', 'name', 'character']