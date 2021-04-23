from rest_framework.routers import DefaultRouter
from OptimizerRestAPI.views import ChemicalElementModelViewset, CommodityModelViewset, ChemicalCompsModelViewset

router = DefaultRouter()


router.register(r'chemical-element', ChemicalElementModelViewset, basename='chemical_element')
router.register(r'commodity', CommodityModelViewset, basename='commodities')
router.register(r'chemical-composition', ChemicalCompsModelViewset, basename='chemical_composition')




