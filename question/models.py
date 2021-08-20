from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.TextField()
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE)


class Answer(models.Model):
    answer = models.CharField(max_length=150)
