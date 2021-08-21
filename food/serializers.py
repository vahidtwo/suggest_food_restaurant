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
    tags = TagSerializer(many=True, read_only=True)
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Food
        fields = '__all__'


class SuggestFoodSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    exercises = ExerciseSerializer(many=True, read_only=True)
    sub_tag_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Food
        fields = '__all__'
        extra_kwargs = {
            "image": {'read_only': True},
            'price': {'read_only': True},
            'title': {'read_only': True},
            'description': {'read_only': True},
            'fat': {'read_only': True},
            'kilo_calories': {'read_only': True},
        }
