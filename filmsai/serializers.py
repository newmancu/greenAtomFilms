from rest_framework import serializers as ser
from filmsai import models


class FilmsBaseSerializer(ser.ModelSerializer):
    
    class Meta:
        model = models.Films
        fields = '__all__'
        
        
class CommentBaseSerializer(ser.ModelSerializer):
    
    class Meta:
        model = models.Comment
        fields = '__all__'
        read_only_fields = ('rating', 'assesment')

        