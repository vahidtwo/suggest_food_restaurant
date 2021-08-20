from rest_framework import serializers

from question.models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer']


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer('answer', many=True)

    class Meta:
        model = Question
        fields = '__all__'
