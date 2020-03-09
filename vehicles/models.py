from django.db import models


class Make(models.Model):
    name = models.CharField(max_length=100)

class Model(models.Model):
    name = models.CharField(max_length=100)
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name='models')

class Trim(models.Model):
    name = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='trims')
    year = models.IntegerField()
