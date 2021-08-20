from django.urls import path

from food.api import ListCreateFoodApi, DetailUpdateDeleteFoodApi, ListCreateTagApi, DetailUpdateDeleteTagApi, \
    ListCreateExerciseApi, DetailUpdateDeleteExerciseApi

urlpatterns = [
    path('food/', ListCreateFoodApi.as_view(), name='foods'),
    path('food/<int:pk>', DetailUpdateDeleteFoodApi.as_view(), name='food'),
    path('tag/', ListCreateTagApi.as_view(), name='tags'),
    path('tag/<int:pk>', DetailUpdateDeleteTagApi.as_view(), name='tag'),
    path('exercise/', ListCreateExerciseApi.as_view(), name='exercises'),
    path('exercise/<int:pk>', DetailUpdateDeleteExerciseApi.as_view(), name='exercise'),

]
