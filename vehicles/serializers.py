from rest_framework import serializers

from .models import Make, Model, Trim


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = ['id', 'name']

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['id', 'make', 'name']

class TrimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trim
        fields = ['id', 'model', 'name', 'year']
