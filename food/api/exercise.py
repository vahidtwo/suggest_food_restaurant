from rest_framework import generics

from food.models import Exercise
from food.serializers import ExerciseSerializer


class ListCreateExerciseApi(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()


class DetailUpdateDeleteExerciseApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()
