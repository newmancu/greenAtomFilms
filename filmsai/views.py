from rest_framework import viewsets
from filmsai import serializers as ser
from filmsai import models
from filmsai.utils import predict


class FilmsViewSet(viewsets.ModelViewSet):
  serializer_class = ser.FilmsBaseSerializer
  queryset = models.Films.objects.all()

  
class CommentsViewSet(viewsets.ModelViewSet):
  serializer_class = ser.CommentBaseSerializer
  queryset = models.Comment.objects.all()

  def perform_create(self, serializer):
    res = serializer.save()
    predict(res.id)
    return res