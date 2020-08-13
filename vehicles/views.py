from django.http import HttpResponse
from rest_framework import viewsets

from .models import Make, Model, ModelYear, Trim
from .serializers import MakeSerializer, ModelSerializer, ModelYearSerializer, TrimSerializer


def index(request):
    return HttpResponse("EV Demo")


class MakeViewSet(viewsets.ModelViewSet):
    queryset = Make.objects.all()
    serializer_class = MakeSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class ModelYearViewSet(viewsets.ModelViewSet):
    queryset = ModelYear.objects.all()
    serializer_class = ModelYearSerializer


class TrimViewSet(viewsets.ModelViewSet):
    queryset = Trim.objects.all()
    serializer_class = TrimSerializer
