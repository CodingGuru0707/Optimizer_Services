from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from OptimizerRestAPI.serializers import ChemicalElementSerializer, CommoditySerializer, ChemicalCompsSerializer
from OptimizerRestAPI.models import ChemicalElement, ChemicalComps, Commodity



# Create your views here.

class CommodityModelViewset(ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer

class ChemicalElementModelViewset(ModelViewSet):
    queryset = ChemicalElement.objects.all()
    serializer_class = ChemicalElementSerializer

class ChemicalCompsModelViewset(ModelViewSet):
    queryset = ChemicalComps.objects.all()
    serializer_class = ChemicalCompsSerializer



