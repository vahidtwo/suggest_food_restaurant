from django.db import models


# Create your models here.
class Food(models.Model):
    image = models.ImageField(upload_to='media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    tags = models.ManyToManyField('Tag')
    fat = models.IntegerField()
    kilo_calories = models.IntegerField()
    exercise = models.ManyToManyField('Exercise')


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Exercise(models.Model):
    name = models.TextField()
