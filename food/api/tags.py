from rest_framework import generics

from food.models import Tag
from food.serializers import TagSerializer


class ListCreateTagApi(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class DetailUpdateDeleteTagApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
