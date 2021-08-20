from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question[:20]


class Answer(models.Model):
    answer = models.CharField(max_length=150)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answer')

    def __str__(self):
        return self.answer
