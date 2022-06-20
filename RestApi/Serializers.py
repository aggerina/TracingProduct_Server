from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
# from InvProducts.models import Product
from INV.models import Product, Part, BOMS
from Employ.models import Person
from TRACING.models import *
from DetailApp.models import ClientApp, AppDetail


class ClientAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClientApp
        fields = ['__str__', 'App', 'version', 'Description', 'Active', 'Server_Address', 'send_port', 'DataBase_Address',
         'DataBase_Name', 'DatabasePort', 'PASSWORD_SERVER', 'USER_SERVER', 'BarcodeRestart', 'BarcodeShutdown', 'BarcodeProdocer', 'BarcodeRepair']

class AppDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppDetail
        fields = ['title', 'NameApp', 'version', 'Description', 'Active']

class PartSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Part
        fields = ['name', 'PartNumber', 'image', 'description', 'price', 'active', 'slug', 'Quantiti', 'title']

class BOMSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BOMS
        fields = ['name', 'PartNumber', 'image', 'description', 'price', 'active', 'slug', 'Quantiti', 'title']


class ProductSerializers(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    # Part = PartSerializer(many=True, read_only=False)
    BOMS = BOMSerializer(many=True, read_only=False)

    class Meta:
        model = Product

        # fields = ['title','name', 'Product_code', 'Tracebility_code', 'description', 'active', 'image', 'Instructions1','Instructions2', 'Part', 'BOMS']
        fields = ['title','name', 'Product_code', 'Tracebility_code', 'description','BOMS', 'active', 'image','_1_Placing_01', '_2_Placing_01', '_1_Placing_02','_2_Placing_02', '_1_1', '_2_1','_1_2','_2_2','_1_3', '_2_3','_1_4','_2_4', '_1_IT','_1_5','_2_5','_1_6','_2_6','_1_7', '_2_7','_1_8','_2_8','_1_9','_2_9','_1_10','_2_10','_1_11','_2_11','_1_12','_2_12','_1_13','_2_13', '_1_LastTest_01','_2_LastTest_01', '_1_LastTest_02', '_2_LastTest_02', '_1_LastTest_03', '_2_LastTest_03', '_1_LastTest_04', '_2_LastTest_04',  '_1_LastTest_05','_1_Checking','_2_Checking','_1_Kafchini','_2_Kafchini','_1_QC_01','_2_QC_01','_1_QC_02','_2_QC_02','_2_Boxing_01','_1_Boxing_01','_1_Repair' ,'_2_Repair', '_2_IT' ]
        # fields = ['__all__']

# class EmploySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Person
#         fields = [ 'Name', 'LastName', 'CodeOperator', 'StartBarcode', 'StopBarcode', 'Image', 'Start']


class Detail_EmploySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = [ 'TelephonNumber','Address', 'Name', 'LastName', 'CodeOperator', 'StartBarcode', 'StopBarcode', 'Image', 'Start']


class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ['title', 'StationNumber', 'Active']




class PersonSerializer( serializers.HyperlinkedModelSerializer):
    lookup_field = "CodeOperator"
    view_name = "device_connected"

    class Meta:
        model = Person


        fields = ['Name', 'LastName', 'CodeOperator', 'StartBarcode', 'StopBarcode', 'Image']
class StationRelatedSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Station
        fields = ['title', 'StationNumber', 'Active']

class Device_ConnectedSerializers(serializers.HyperlinkedModelSerializer):

    Operators = PersonSerializer(many=True, read_only=False)

    Stations = StationRelatedSerializer(many=True , read_only=False)
    # Stations = StationRelatedSerializer(many=True, queryset=Station.objects.all() )

    class Meta:

        model = Device_Connected
        fields = ['title', 'Operators', 'Data', 'time', 'Stations']



class Opc_ProductSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    Product =  ProductSerializers(many=True, read_only=False)

    class Meta:
        model = Opc_Product
        fields = ['title', 'Product', 'Opc_Order', 'Order_code_Product', 'Instructions', 'picture', 'time','date']


class OrdersSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    Product = ProductSerializers(many=True, read_only=False)
    class Meta:
        model = Orders
        fields = ['title', 'code', 'Recive_Data', 'MaximumTime','Count', 'Product']

class Recipt_outSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipt_out
        fields = ['cod_product', 'description_prodact', 'Qountiti', 'order_code', 'curent_data', 'Cod_Operator',
                  'destinastion_store', 'sorce_store','form_number', 'position_out', 'center_cost']


class Sum_Recipt_outSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sum_Recipt_out
        fields = ['product_cod_SUM', 'DESCRIPTION', 'Sum_all_Pro', 'order_cod', 'form_number']

class Tracebility_codeSerializer(serializers.HyperlinkedModelSerializer):
    order = OrdersSerializer(many=True, read_only=False)
    max_page_size = 100
    class Meta:

        model = TracebilityCode
        fields = ['Tracebility_code', 'Date', 'order']



class  Station_to_orderSerializer(serializers.HyperlinkedModelSerializer):
    StationNumber = StationSerializer(many=True, read_only=False)
    order = OrdersSerializer(many=True, read_only=False)
    person = PersonSerializer(many=True, read_only=False)
    class Meta:
        model = Station_to_order
        fields =  ['StationNumber', 'order', 'person', 'Time_for_work']


class Construction_processesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Construction_processes
        fields = ['title', 'Order', 'Description', 'Level', 'guide']

class OpcDefualtSerializer(serializers.HyperlinkedModelSerializer):
    ConstructionProcesses = Construction_processesSerializer(many=True , read_only=False)


    class Meta:
        model = OpcDefualt
        fields = ['title', 'ConstructionProcesses']

class Opc_To_StationsSerializer(serializers.HyperlinkedModelSerializer):
    Operator = Detail_EmploySerializer(many=True, read_only=False)
    station = StationSerializer(many=True, read_only=False)
    opc = OpcDefualtSerializer(many=True, read_only=False)
    class Meta:
        model =Opc_To_Stations
        fields = ['title', 'Operator', 'station', 'opc', 'Date']


class Tracing_ProductsSerializer(serializers.HyperlinkedModelSerializer):
    Operator = Detail_EmploySerializer(many=True, read_only=False)
    station = StationSerializer(many=True, read_only=False)
    order = OrdersSerializer(many=True, read_only=False)
    product = ProductSerializers(many=True, read_only=False)
    tracebility_code = Tracebility_codeSerializer(many=True, read_only=False)

    class Meta:
        model = Tracing_Products
        fields = ['Operator', 'station', 'order', 'product', 'tracebility_code', 'Date', 'Time']


class  TracebilityDataSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TracebilityData
        fields = ['Operator', 'Station', 'Order', 'Product', 'tracebilityCode', 'Date', 'Time']

class UnknownOperatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

        model = UnknownOperator
        fields = ['station', 'tracebilityCode','Order', 'Product', 'Date', 'Time']




class RepairStationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RepairStation
        fields  = ['Operator', 'Station','Description', 'Order','Entery','Exit', 'Product','Cuase', 'State', 'tracebilityCode', 'Date', 'Time']
