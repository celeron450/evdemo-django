from rest_framework import serializers

from .models import Make, Model, ModelYear, Trim


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

    class Meta:
        model = ModelYear
        fields = ['id', 'model', 'year']


class TrimSerializer(serializers.ModelSerializer):
    model_year = ModelYearSerializer()

    class Meta:
        model = Trim
        fields = ['id', 'model_year', 'name']
