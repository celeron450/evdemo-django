from django.db import models


class Make(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Model(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(self.make, self.name)


class ModelYear(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='model_years')
    year = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.year, self.model)


class Trim(models.Model):
    model_year = models.ForeignKey(ModelYear, on_delete=models.CASCADE, related_name='trims')
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(self.model_year, self.name)
