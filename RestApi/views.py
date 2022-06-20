from builtins import id
from functools import reduce

from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from rest_framework import permissions
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from  django.http import  Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, action
from INV.models import Product, Part
from Employ.models import Person
from rest_framework import viewsets
from RestApi.Serializers import *
# ProductSerializers , Detail_EmploySerializer, StationSerializer,\
#     Device_ConnectedSerializers, Opc_ProductSerializer, OrdersSerializer, Recipt_outSerializer, Sum_Recipt_outSerializer,\
#     Tracebility_codeSerializer, Station_to_orderSerializer, Construction_processesSerializer, OpcDefualtSerializer,\
#     Opc_To_StationsSerializer, Tracing_ProductsSerializer, PartSerializer, TracebilityDataSerialiser, AppDetailSerializer, ClientAppSerializer
from TRACING.models import *
#
# Station, Device_Connected, Opc_Product, Orders,Recipt_out, Sum_Recipt_out, TracebilityCode,\
#     Station_to_order, Construction_processes ,Opc_To_Stations, Tracing_Products, TracebilityData
from DetailApp.models import ClientApp, AppDetail

class GetDetailApp(viewsets.ModelViewSet):
    queryset = AppDetail.objects.all()
    serializer_class = AppDetailSerializer

class GetClientApp(viewsets.ModelViewSet):
    queryset = ClientApp.objects.all()
    serializer_class = ClientAppSerializer

class EmployViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = Detail_EmploySerializer

######################################################

class DetailPerson( viewsets.ModelViewSet):

    queryset = Person.objects.all()
    lookup_field = 'StartBarcode'

    serializer_class = Detail_EmploySerializer
    # lookup_fields = ['StartBarcode', 'StopBarcode']
    @action(detail=True, methods=['GET'])
    def get_Person(self,request, StartBarcode):
        if request.method == "GET":
            try:
                person = Person.objects.get(StartBarcode=StartBarcode)
                person.Start =True
                person.save()
                serializer = Detail_EmploySerializer(person)
                return Response(serializer.data)
            except:
                pass
            try:
                person = Person.objects.get(StopBarcode=StartBarcode)
                person.Start = False
                person.save()
                serializer = Detail_EmploySerializer(person)
                return Response(serializer.data)
            except:
                pass


            # serializer = Detail_EmploySerializer(person)
            # return Response(serializer.data)

    def update(self, request, *args, **kwargs):

        if request.method == "PUT":

            person = Person.objects.get(StartBarcode=self.kwargs['StartBarcode'])
            # except :
            #     pass
            # try:
            #     person = Person.objects.get(StopBarcode=self.kwargs['StartBarcode'])
            #



            # if person.StartBarcode == self.kwargs['StartBarcode']:
            #     person.Start = True
            #     person.save()
            serializer = Detail_EmploySerializer(person, data=request.data)
            if serializer.is_valid():
                serializer.save()

            print(self.kwargs['StartBarcode'])
            print(person.StartBarcode)
            if person.StartBarcode == self.kwargs['StartBarcode']:
                person.Start = True
                person.save()
            # if person.Start == True:
            #     person.Start = False
            #     person.save()
            # elif person.Start == False:
            #     person.Start = True
            #     person.save()
            return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:

                product = self.get_object()
                self.perform_destroy(product)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)


class GetParts(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    lookup_field = 'PartNumber'


    @action(detail=True, methods=['GET'])
    def get_part(self,request, PartNumber):
        if request.method == "GET":

            part = Product.objects.get(PartNumber=PartNumber)

            serializer = PartSerializer(part)
            return Response(serializer.data)
    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = Part.objects.get(PartNumber=self.kwargs['PartNumber'])
            serializer = PartSerializer(instance, data=request.data,)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                part  = self.get_object()
                self.perform_destroy(part)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)

class GetBOMS(viewsets.ModelViewSet):
    queryset = BOMS.objects.all()
    serializer_class = BOMSerializer
    lookup_field = 'PartNumber'


    @action(detail=True, methods=['GET'])
    def get_part(self,request, PartNumber):
        if request.method == "GET":

            part = Product.objects.get(PartNumber=PartNumber)

            serializer = BOMSerializer(part)
            return Response(serializer.data)
    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = BOMS.objects.get(PartNumber=self.kwargs['PartNumber'])
            serializer = BOMSerializer(instance, data=request.data,)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                bom  = self.get_object()
                self.perform_destroy(bom)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)



class DetailProduct(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    lookup_field = 'Product_code'

    serializer_class = ProductSerializers

    @action(detail=True, methods=['GET'])
    def get_peroduct(self,request, Product_code):

        product = Product.objects.get(Product_code=Product_code)

        serializer = ProductSerializers(product)
        return Response(serializer.data)


class GetDatailProducts(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    lookup_field = 'Product_code'

    serializer_class = ProductSerializers


    @action(detail=True, methods=['GET'])
    def get_product(self,request, Product_code):
        if request.method == "GET":

            product = Product.objects.get(Product_code=Product_code)

            serializer = ProductSerializers(product)
            return Response(serializer.data)


    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            product = Product.objects.get(Product_code=self.kwargs['Product_code'])

            serializer = ProductSerializers(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:

                product = self.get_object()
                self.perform_destroy(product)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)
    # def create(self, request, *args, **kwargs):
    #     if request.method == 'post':
    #         product = Product.objects.get()

class GetStations(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    lookup_field = 'StationNumber'


    def update(self, request, *args, **kwargs):
        data_in = request.data
        if request.method == "PUT":
            instance = Station.objects.get(StationNumber=self.kwargs['StationNumber'])
            serializer = StationSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:

                station = self.get_object()
                self.perform_destroy(station)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)


class GetActiveStation(APIView):
    def get(self, request):

        activeStation = Station.objects.filter(Active=True)
        serializer = StationSerializer(activeStation, many=True)
        return Response(serializer.data)



class GetDevice_Connected(viewsets.ModelViewSet):
    queryset =  Device_Connected.objects.all()
    serializer_class = Device_ConnectedSerializers
    lookup_field = 'Stations'
    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = Device_Connected.objects.get(Stations=self.kwargs['Stations'])
            serializer = Device_ConnectedSerializers(instance, data=request.data,)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:

                connectedDevice  = self.get_object()
                self.perform_destroy(connectedDevice)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)




class GetOpc_Products(viewsets.ModelViewSet):
    queryset =  Opc_Product.objects.all()
    serializer_class = Opc_ProductSerializer
    lookup_field = 'Product'
    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = Opc_Product.objects.get(Product=self.kwargs['Product'])
            serializer = Opc_ProductSerializer(instance, data=request.data,)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:

                opc_product  = self.get_object()
                self.perform_destroy(opc_product)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)

class GetOrders(viewsets.ModelViewSet):

    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    lookup_field = 'code'

    def update(self, request, *args, **kwargs):

        if request.method == "put":
            instance = Orders.objects.get(Product=self.kwargs['code'])
            serializer = OrdersSerializer(instance, data=request.data,)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #      device = Device.objects.filter(device_id=request.data['imei'])
    #      device.registration_id = request.data['regId']
    #      device.save()
    #      serializer = DeviceSerializer(device)
    #     return Response({'ok': 'oks'})



    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:

                order  = self.get_object()
                self.perform_destroy(order)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)


class GetReciptOut(viewsets.ModelViewSet):

    queryset = Recipt_out.objects.all()
    serializer_class = Recipt_outSerializer
    lookup_field = 'form_number'
    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = Recipt_out.objects.get(Product=self.kwargs['form_number'])
            serializer = Recipt_outSerializer(instance, data=request.data,)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                recipt  = self.get_object()
                self.perform_destroy(recipt)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)




class  GetSum_Recipt_out(viewsets.ModelViewSet):

    queryset = Sum_Recipt_out.objects.all()
    serializer_class = Sum_Recipt_outSerializer
    lookup_field = 'form_number'
    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = Sum_Recipt_out.objects.get(form_number=self.kwargs['form_number'])
            serializer = Sum_Recipt_outSerializer(instance, data=request.data,)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                sum_recipt  = self.get_object()
                self.perform_destroy(sum_recipt)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)


class GetTracebilityBettween(viewsets.ModelViewSet):
    queryset = TracebilityCode.objects.all()
    serializer_class = Tracebility_codeSerializer
    lookup_field = 'Tracebility_code'

    def get_queryset(self):
        tracingCode1 = self.queryset.filter(Tracebility_code='g39gNbbK').first()
        id1  = tracingCode1.id
        print(f"id 1 {id1}")
        tracingCode2 = self.queryset.filter(Tracebility_code='BM6kBed4').first()
        id2 = tracingCode2.id
        print(f"id 2 {id2}")

        # BetweenQuery = self.queryset.filter(range(id1, id2))
        BetweenQuery = self.queryset.filter(pk__gt=id1, pk__lte=id2)
        # self.queryset = TracebilityCode.objects.filter()
        return BetweenQuery
    # def GetBarcodes(self,*args,  **kwargs):
    #     tracingCode1 = self.queryset.filter(Tracebility_code='ApovWRZn').first()
    #     id1  = tracingCode1.id
    #     print(f"id 1 {id1}")
    #     tracingCode2 = self.queryset.filter(Tracebility_code='aPZeurEa').first()
    #     id2 = tracingCode2.id
    #     print(f"id 2 {id2}")
    #
    #     # BetweenQuery = self.queryset.filter(range(id1, id2))
    #     BetweenQuery = self.queryset.filter(pk__gt=id1, pk__lte=id2)
    #     # self.queryset = TracebilityCode.objects.filter()
    #     return BetweenQuery

class GetTracebility_code(viewsets.ModelViewSet):

    queryset = TracebilityCode.objects.all()
    serializer_class = Tracebility_codeSerializer
    lookup_field = 'Tracebility_code'

    # def get_queryset(self):
    #     query = self.request.GET.get('query', None)
    #
    #     BetweenQuery =  self.queryset.filter(range('gtMSvkKt', 'KCjdU6JA'))
    #     # self.queryset = TracebilityCode.objects.filter()
    #     return BetweenQuery

    # def get_queryset(self):
    #     qs = super(GetTracebility_code, self).get_queryset()
    #     qs = qs.filter()
    #     return qs
    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = TracebilityCode.objects.get(TracebilityCode=self.kwargs['Tracebility_code'])
            serializer = Tracebility_codeSerializer(instance, data=request.data,)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                sum_recipt  = self.get_object()
                self.perform_destroy(sum_recipt)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)


class GetStation_to_order(viewsets.ModelViewSet):
    queryset = Station_to_order.objects.all()
    serializer_class = Station_to_orderSerializer
    lookup_field = 'StationNumber'
    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = Station_to_order.objects.get(StationNumber=self.kwargs['StationNumber'])
            serializer = Station_to_orderSerializer(instance, data=request.data,)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                station_to_order  = self.get_object()
                self.perform_destroy(station_to_order)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)


class GetConstruction_processes(viewsets.ModelViewSet):
    queryset = Construction_processes.objects.all()
    serializer_class = Construction_processesSerializer
    lookup_field = 'code'
    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = Construction_processes.objects.get(code=self.kwargs['code'])
            serializer = Construction_processesSerializer(instance, data=request.data,)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                conststration  = self.get_object()
                self.perform_destroy(conststration)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)




class GetOpcDefault(viewsets.ModelViewSet):
    queryset = Opc_Product.objects.all()
    serializer_class = OpcDefualtSerializer
    lookup_field = 'ConstructionProcesses'
    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = Construction_processes.objects.get(ConstructionProcesses=self.kwargs['ConstructionProcesses'])
            serializer = Construction_processesSerializer(instance, data=request.data,)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                opc  = self.get_object()
                self.perform_destroy(opc)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)


class GetOpc_To_Stations(viewsets.ModelViewSet):
    queryset = Opc_To_Stations.objects.all()
    serializer_class = Opc_To_StationsSerializer
    lookup_field = 'station'
    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = Opc_To_Stations.objects.get(station=self.kwargs['station'])
            serializer = Opc_To_StationsSerializer(instance, data=request.data,)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                opc_to_Station  = self.get_object()
                self.perform_destroy(opc_to_Station)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)



class GetTracing_Products(viewsets.ModelViewSet):
    queryset = Tracing_Products.objects.all()
    serializer_class = Tracing_ProductsSerializer
    lookup_field = 'station'
    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = Tracing_Products.objects.get(station=self.kwargs['station'])
            serializer = Tracing_ProductsSerializer(instance, data=request.data,)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                tracing_product  = self.get_object()
                self.perform_destroy(Tracing_Products)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)





class GetTracebilityData(viewsets.ModelViewSet):
    queryset = TracebilityData.objects.all()
    serializer_class = TracebilityDataSerialiser
    lookup_field = 'Order'
    def update(self, request, *args, **kwargs):
        if request.method == "PUT":
            instance = TracebilityData.objects.get(Order=self.kwargs['Order'])
            serializer = TracebilityDataSerialiser(instance, data=request.data, )
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                tracebility  = self.get_object()
                self.perform_destroy(tracebility)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)




class GetUnknownOperator(viewsets.ModelViewSet):

    queryset = UnknownOperator.objects.all()
    serializer_class = UnknownOperatorSerializer
    lookup_field = 'tracebilityCode'

    @action(detail=True, methods=['GET'])
    def get_UnknownOperator(self,request, tracebilityCode):
        if request.method == "GET":

            unknownOperator = UnknownOperator.objects.filter(tracebilityCode=tracebilityCode)

            serializer = UnknownOperatorSerializer(unknownOperator, many=True)
            return Response(serializer.data)
    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = UnknownOperator.objects.filter(tracebilityCode=self.kwargs['tracebilityCode'])
            serializer = UnknownOperatorSerializer(instance, data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                bom  = self.get_object()
                self.perform_destroy(bom)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)

class GetUnknownOperators(APIView):
    # queryset = UnknownOperator.objects.filter()
    # serializer_class = UnknownOperatorSerializer
    # lookup_field = 'tracebilityCode'
    #

    def get(self, request, tracebilityCode):
        if request.method == "GET":
            unknownOperator = UnknownOperator.objects.filter(tracebilityCode=tracebilityCode)
            serializer =  UnknownOperatorSerializer(unknownOperator, many=True)
            return Response(serializer.data)
    def post(self, request):
        if request.method == "POST":

            serializer = UnknownOperatorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                # return Response(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,  tracebilityCode):
        if request.method == 'DELETE':
            unknownOperator = UnknownOperator.objects.filter(tracebilityCode=tracebilityCode)
            unknownOperator.delete()
            return  JsonResponse({"Massage": "UnknownOperator log deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class GetRepairProduct(viewsets.ModelViewSet):
    queryset = RepairStation.objects.all()
    serializer_class = RepairStationSerializer
    lookup_field = 'tracebilityCode'


    @action(detail=True, methods=['GET'])
    def get_RepairProduct(self, request, tracebilityCode):
        if request.method == "GET":
            repairStation = RepairStation.objects.filter(tracebilityCode=tracebilityCode)

            serializer = RepairStationSerializer(repairStation, many=True)
            return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def get(self, request, tracebilityCode):
        if request.method == "GET":
            repairStation = RepairStation.objects.filter(tracebilityCode=tracebilityCode)

            serializer = RepairStationSerializer(repairStation, many=True)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):

        if request.method == "PUT":
            instance = RepairStation.objects.filter(tracebilityCode=self.kwargs['tracebilityCode'])
            serializer = RepairStationSerializer(instance, data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        if request.method == "DELETE":
            try:
                bom = self.get_object()
                self.perform_destroy(bom)
            except Http404:
                pass
            return Response(status=status.HTTP_204_NO_CONTENT)


