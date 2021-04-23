from rest_framework import serializers
from OptimizerRestAPI. models import ChemicalElement, ChemicalComps, Commodity



class ChemicalElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemicalElement
        fields = "__all__"

class ChemicalCompsSerializer(serializers.ModelSerializer):
    chem_ele = ChemicalElementSerializer()
    class Meta:
        model = ChemicalComps
        fields = ('id', 'chem_ele', 'percentage')

class CommoditySerializer(serializers.ModelSerializer):
    chemical_composition = ChemicalCompsSerializer(many=True,read_only=True)
    class Meta:
        model = Commodity
        fields = ('id', 'name', 'inventory', 'price', 'chemical_composition')


