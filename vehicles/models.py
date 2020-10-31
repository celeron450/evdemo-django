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

    @property
    def available_drive_types(self):
        return DriveType.objects.filter(trim__model_year=self).distinct().order_by('name')

    @property
    def seating_capacity_range(self):
        seating_capacity_list = self.trims.filter(seating_capacity__isnull=False).values_list('seating_capacity', flat=True)
        return (min(seating_capacity_list), max(seating_capacity_list)) if seating_capacity_list else (None, None)

    @property
    def mpge_city_range(self):
        mpge_city_list = self.trims.filter(mpge_city__isnull=False).values_list('mpge_city', flat=True)
        return (min(mpge_city_list), max(mpge_city_list)) if mpge_city_list else (None, None)

    @property
    def mpge_highway_range(self):
        mpge_highway_list = self.trims.filter(mpge_highway__isnull=False).values_list('mpge_highway', flat=True)
        return (min(mpge_highway_list), max(mpge_highway_list)) if mpge_highway_list else (None, None)

    @property
    def mpge_combined_range(self):
        mpge_combined_list = self.trims.filter(mpge_combined__isnull=False).values_list('mpge_combined', flat=True)
        return (min(mpge_combined_list), max(mpge_combined_list)) if mpge_combined_list else (None, None)

    @property
    def range_city_range(self):
        range_city_list = self.trims.filter(range_city__isnull=False).values_list('range_city', flat=True)
        return (min(range_city_list), max(range_city_list)) if range_city_list else (None, None)

    @property
    def range_highway_range(self):
        range_highway_list = self.trims.filter(range_highway__isnull=False).values_list('range_highway', flat=True)
        return (min(range_highway_list), max(range_highway_list)) if range_highway_list else (None, None)

    @property
    def range_combined_range(self):
        range_combined_list = self.trims.filter(range_combined__isnull=False).values_list('range_combined', flat=True)
        return (min(range_combined_list), max(range_combined_list)) if range_combined_list else (None, None)

    @property
    def charge_time_hours_240v_range(self):
        charge_time_hours_240v_list = self.trims.filter(charge_time_hours_240v__isnull=False).values_list('charge_time_hours_240v', flat=True)
        return (min(charge_time_hours_240v_list), max(charge_time_hours_240v_list)) if charge_time_hours_240v_list else (None, None)

    @property
    def kwh_per_100mi_range(self):
        kwh_per_100mi_list = self.trims.filter(kwh_per_100mi__isnull=False).values_list('kwh_per_100mi', flat=True)
        return (min(kwh_per_100mi_list), max(kwh_per_100mi_list)) if kwh_per_100mi_list else (None, None)

    @property
    def horsepower_range(self):
        horsepower_list = self.trims.filter(horsepower__isnull=False).values_list('horsepower', flat=True)
        return (min(horsepower_list), max(horsepower_list)) if horsepower_list else (None, None)

    @property
    def torque_range(self):
        torque_list = self.trims.filter(torque__isnull=False).values_list('torque', flat=True)
        return (min(torque_list), max(torque_list)) if torque_list else (None, None)

    @property
    def zero_to_sixty_seconds_range(self):
        zero_to_sixty_seconds_list = self.trims.filter(zero_to_sixty_seconds__isnull=False).values_list('zero_to_sixty_seconds', flat=True)
        return (min(zero_to_sixty_seconds_list), max(zero_to_sixty_seconds_list)) if zero_to_sixty_seconds_list else (None, None)

    @property
    def starting_msrp_range(self):
        starting_msrp_list = self.trims.filter(starting_msrp__isnull=False).values_list('starting_msrp', flat=True)
        return (min(starting_msrp_list), max(starting_msrp_list)) if starting_msrp_list else (None, None)


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
