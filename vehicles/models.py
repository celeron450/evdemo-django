from django.db import models


class MediaLicense(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class BodyStyle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DriveType(models.Model):
    name = models.CharField(max_length=100)

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
    body_style = models.ForeignKey(BodyStyle, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} {}'.format(self.year, self.model)


class Trim(models.Model):
    model_year = models.ForeignKey(ModelYear, on_delete=models.CASCADE, related_name='trims')
    name = models.CharField(max_length=100)
    drive_type = models.ForeignKey(DriveType, null=True, blank=True, on_delete=models.SET_NULL)
    seating_capacity = models.IntegerField(null=True, blank=True)
    mpge_city = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    mpge_highway = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    mpge_combined = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    range_city = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    range_highway = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    range_combined = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    charge_time_hours_240v = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    kwh_per_100mi = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    horsepower = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    torque = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    zero_to_sixty_seconds = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    starting_msrp = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.model_year, self.name)
