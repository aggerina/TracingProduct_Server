from django.urls import path, include, re_path
from rest_framework import routers

from RestApi.views import *

router = routers.DefaultRouter()
router.register(r'Persons', DetailPerson, basename="DetailPerson")
router.register(r'Parts' ,GetParts , basename="GetParts")
router.register(r'BOMS' ,GetBOMS , basename="GetBOMS")
router.register(r'Products', GetDatailProducts, basename="DetailProducts")
# router.register(r'API_Person/<int:PersonalCode>', views.DetailPersonal, basename='code')
router.register('Stations', GetStations, basename="Stations" )
router.register(r'DeviceConnedted', GetDevice_Connected, basename="connectedDevices")
router.register(r'opcProduct', GetOpc_Products, basename="opcProduct")
router.register(r'Orders', GetOrders, basename="orders")
router.register(r'ReciptOut', GetReciptOut, basename="reciptout")
router.register(r'Sum_ReciptOut', GetSum_Recipt_out, basename="Sum_reciptout")
router.register(r'Tracebility', GetTracebility_code, basename="Tracebility")
router.register(r'Tracebilitybeetween', GetTracebilityBettween, basename="Tracebilitybeetween")
router.register(r'Station_to_order', GetStation_to_order, basename="GetStation_to_order")
router.register(r'Construction_processes', GetConstruction_processes, basename="GetConstruction_processes")
router.register(r'OpcDefault', GetOpcDefault, basename="GetOpcDefault")
router.register(r'Opc_To_Stations', GetOpc_To_Stations, basename="GetOpc_To_Stations")
router.register(r'Tracing_Products' ,GetTracing_Products , basename="GetOpc_To_Stations")
router.register(r'TracebilityData' ,GetTracebilityData , basename="GetTracebilityData")
router.register(r'AppDetail' ,GetDetailApp , basename="GetDetailApp ")
router.register(r'ClientApp' ,GetClientApp , basename="GetClientApp")
router.register(r'UnknownOperator' ,GetUnknownOperator , basename="GetUnknownOperator")
router.register(r'RepairProduct' ,GetRepairProduct , basename="GetRepairProduct")


urlpatterns = [
    path('list/', include(router.urls)),
    # path(r'Person/<PersonalCode>', DetailPersonal.as_view()),
    # path(r'Persons/', EmployViewSet.as_view({'get': 'list'})),
    path('Person/<startbarcode>', DetailPerson.as_view({'get': 'retrieve',})),

    path('Product/<Product_code>', DetailProduct.as_view({'get': 'retrieve',})),
    path('ActiveStation/', GetActiveStation.as_view()),
    path('UnknownOperators/<str:tracebilityCode>', GetUnknownOperators.as_view()),


]