from django.db import models


class StudentModel(models.Model):

    stu_name = models.CharField(max_length=500)
    stu_city = models.CharField(max_length=500)
    stu_age = models.IntegerField()

    def __str__(self):
        return self.stu_name


class SuperMarket(models.Model):

    market_name = models.CharField(max_length = 400)
    market_place = models.CharField(max_length = 300)

    def __str__(self):

        return self.market_name


