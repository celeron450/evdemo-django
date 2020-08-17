from rest_framework import serializers

from .models import Make, MediaLicense, Model, ModelYear, Trim


class MediaLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaLicense
        fields = ['id', 'name', 'url']


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

    class Meta:
        model = ModelYear
        fields = [
            'id', 'model', 'year', 'manufacturer_url', 'image_url', 'thumbnail_url',
            'image_attribution_title', 'image_attribution_url', 'image_attribution_author',
            'image_attribution_author_url', 'image_license',
        ]


class TrimSerializer(serializers.ModelSerializer):
    model_year = ModelYearSerializer()

    class Meta:
        model = Trim
        fields = ['id', 'model_year', 'name']
