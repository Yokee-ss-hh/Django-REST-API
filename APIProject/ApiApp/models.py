from django.db import models

# Create your models here.


class DrinksModel(models.Model):

    drink_name = models.CharField(max_length=200)
    drink_description = models.CharField(max_length=500)
    quantity_available = models.IntegerField(max_length=100)

    def __str__(self):

        return self.drink_name




