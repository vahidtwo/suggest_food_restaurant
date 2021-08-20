from rest_framework import serializers

from question.models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer()

    class Meta:
        model = Quetion
        fields = '__all__'
