from rest_framework import generics

from question.models import Question
from question.serializers import QuestionSerializer


class ListQuestion(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class RetrieveQuestion(generics.RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
