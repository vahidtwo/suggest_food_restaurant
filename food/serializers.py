from rest_framework import serializers

from food.models import Food, Tag, Exercise


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Food
        fields = '__all__'
