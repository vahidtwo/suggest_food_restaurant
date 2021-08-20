from rest_framework import generics

from food.models import Food
from food.serializers import FoodSerializer


class ListCreateFoodApi(generics.ListCreateAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class DetailUpdateDeleteFoodApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
