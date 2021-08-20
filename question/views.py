from rest_framework import generics

from question.models import Question


class ListQuestion(generics.ListAPIView):
    serializer_class = Question
    queryset = Question.objects.all()


class RetrieveQuestion(generics.RetrieveAPIView):
    serializer_class = Question
    queryset = Question.objects.all()
