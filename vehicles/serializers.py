from rest_framework import serializers

from .models import BodyStyle, DriveType, Make, MediaLicense, Model, ModelYear, Trim


class MediaLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaLicense
        fields = ['id', 'name', 'url']


class BodyStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyStyle
        fields = ['id', 'name']


class DriveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveType
        fields = ['id', 'name']


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = ['id', 'name']


class ModelSerializer(serializers.ModelSerializer):
    make = MakeSerializer()

    class Meta:
        model = Model
        fields = ['id', 'make', 'name']


class ModelYearSerializer(serializers.ModelSerializer):
    model = ModelSerializer()
    image_license = MediaLicenseSerializer()
    body_style = BodyStyleSerializer()
    available_drive_types = DriveTypeSerializer(many=True)

    class Meta:
        model = ModelYear
        fields = [
            'id', 'model', 'year', 'manufacturer_url', 'image_url', 'thumbnail_url',
            'image_attribution_title', 'image_attribution_url', 'image_attribution_author',
            'image_attribution_author_url', 'image_license', 'body_style', 'available_drive_types',
            'seating_capacity_range', 'mpge_city_range', 'mpge_highway_range', 'mpge_combined_range',
            'range_city_range', 'range_highway_range', 'range_combined_range', 'charge_time_hours_240v_range',
            'kwh_per_100mi_range', 'horsepower_range', 'torque_range', 'zero_to_sixty_seconds_range',
            'starting_msrp_range',
        ]


class TrimSerializer(serializers.ModelSerializer):
    drive_type = DriveTypeSerializer()

    class Meta:
        model = Trim
        fields = [
            'id', 'model_year_id', 'name', 'drive_type', 'seating_capacity', 'mpge_city',
            'mpge_highway', 'mpge_combined', 'range_city', 'range_highway', 'range_combined',
            'charge_time_hours_240v', 'kwh_per_100mi', 'horsepower', 'torque',
            'zero_to_sixty_seconds', 'starting_msrp',
        ]


class ModelYearFullSerializer(serializers.ModelSerializer):
    model = ModelSerializer()
    image_license = MediaLicenseSerializer()
    body_style = BodyStyleSerializer()
    trims = TrimSerializer(many=True)

    class Meta:
        model = ModelYear
        fields = [
            'id', 'model', 'year', 'manufacturer_url', 'image_url', 'thumbnail_url',
            'image_attribution_title', 'image_attribution_url', 'image_attribution_author',
            'image_attribution_author_url', 'image_license', 'body_style', 'trims',
        ]
