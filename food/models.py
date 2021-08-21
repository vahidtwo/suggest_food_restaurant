from django.db import models


# Create your models here.
class Food(models.Model):
    image = models.ImageField(upload_to='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    tags = models.ManyToManyField('Tag')
    fat = models.IntegerField()
    kilo_calories = models.IntegerField()
    exercises = models.ManyToManyField('Exercise', null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
