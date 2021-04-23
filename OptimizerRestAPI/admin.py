from django.contrib import admin
from OptimizerRestAPI.models import ChemicalElement, ChemicalComps, Commodity
# from django import ModelAdmin

# Register your models here.

admin.site.register([ChemicalElement, ChemicalComps, Commodity])





