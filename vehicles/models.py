from django.db import models


class MediaLicense(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


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
    manufacturer_url = models.CharField(max_length=2000, null=True, blank=True)
    image_url = models.CharField(max_length=2000, null=True, blank=True)
    thumbnail_url = models.CharField(max_length=2000, null=True, blank=True)
    image_attribution_title = models.CharField(max_length=100, null=True, blank=True)
    image_attribution_url = models.CharField(max_length=2000, null=True, blank=True)
    image_attribution_author = models.CharField(max_length=100, null=True, blank=True)
    image_attribution_author_url = models.CharField(max_length=2000, null=True, blank=True)
    image_license = models.ForeignKey(MediaLicense, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} {}'.format(self.year, self.model)


class Trim(models.Model):
    model_year = models.ForeignKey(ModelYear, on_delete=models.CASCADE, related_name='trims')
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(self.model_year, self.name)
