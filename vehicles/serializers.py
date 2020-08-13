from rest_framework import serializers

from .models import Make, Model, ModelYear, Trim


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = ['id', 'name']


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'make', 'name']


class ModelYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelYear
        fields = ['id', 'model', 'year']


class TrimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trim
        fields = ['id', 'model_year', 'name']
