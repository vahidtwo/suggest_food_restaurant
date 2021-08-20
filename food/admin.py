from django.contrib import admin

# Register your models here.
from food.models import Food, Tag, Exercise

admin.site.register(Food)
admin.site.register(Tag)
admin.site.register(Exercise)