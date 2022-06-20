from django.contrib import admin
from TRACING.models import  *



class recipt(admin.ModelAdmin):
    list_display = ('__str__','cod_product','order_code', 'description_prodact', 'Qountiti', 'curent_data', 'Cod_Operator')
    search_fields = [ 'cod_product','order_code', 'description_prodact', 'Qountiti','curent_data', 'Cod_Operator']
    class Meta:
        model = Recipt_out

admin.site.register(Recipt_out, recipt)







class opc_product(admin.ModelAdmin):
    list_display = ('__str__', 'Opc_Order')

    search_fields = ['__str__', 'Opc_Order', 'Opc_Order', 'Order_code_Product']
    class Meta:
        model = Opc_Product

admin.site.register(Opc_Product, opc_product)






class connectDevice(admin.ModelAdmin):
    # list_display = ('__str__', 'CodeOperator', 'DataTime','Stationnumber' )
    list_display = ('__str__', )
    search_fields = ['__str__', ]
    class Meta:
        model = Device_Connected

admin.site.register(Device_Connected, connectDevice)






class tracebility_Code(admin.ModelAdmin):
    list_display = ('__str__', 'Tracebility_code', 'Date', 'time')
    search_fields = ['__str__', 'Date', 'time']
    list_filter = [ 'Date', 'order',]
    filter_vertical =  ['order']

    class Meta:
        model = TracebilityCode

admin.site.register(TracebilityCode, tracebility_Code)






class sum_Recipt_Out(admin.ModelAdmin):
    list_display = ('__str__', 'product_cod_SUM', 'DESCRIPTION')
    search_fields = ['__str__', 'product_cod_SUM', 'DESCRIPTION']
    class Meta:
        model = Sum_Recipt_out

admin.site.register(Sum_Recipt_out, sum_Recipt_Out)




class  Stationnumbers(admin.ModelAdmin):
    list_display =  ('__str__', 'StationNumber', "Active")
    search_fields = ['__str__', 'StationNumber', "Active"]
    class Meta:
        model = Station
admin.site.register(Station, Stationnumbers)





class Station_to_orders(admin.ModelAdmin):
    list_display = ('__str__', )
    search_fields = ['__str__', 'StationNumber', 'order', 'person']
    # filter_horizontal = []

    class Meta:
        model = Station_to_order
admin.site.register(Station_to_order, Station_to_orders)





class ordersAdmin(admin.ModelAdmin):
    # list_display = ('__str__', 'code','ReciveData',"ReciveTime", 'MaximumTime')
    # search_fields = ['__str__', 'code','ReciveData','ReciveTime', 'MaximumTime', 'Product']

    list_display = ('__str__', 'code', 'Count', 'Recive_Data', 'MaximumTime')
    search_fields = [ 'code',]
    # filter_vertical = ['Product']
    filter_horizontal = ['Product',]
    class Meta:
        model = Orders

admin.site.register(Orders, ordersAdmin)




class Admin_Construction_processes(admin.ModelAdmin):
    list_display = ('__str__', 'Order', 'Description','Level')
    search_fields = ['__str__', 'Order', 'name', 'Description','Level']
    class Meta:
        model = Construction_processes

admin.site.register(Construction_processes, Admin_Construction_processes)



class AdminOpcDefualt(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['__str__', 'ConstructionProcesses']
    filter_horizontal = ['ConstructionProcesses']
    # def Get_ConstructionProcesses(self, obj):
    #     return "\n".join([obj.])
    class Meta:
        model = OpcDefualt

admin.site.register(OpcDefualt, AdminOpcDefualt )


class Admin_Opc_To_Stations(admin.ModelAdmin):
    list_display = ["__str__", 'Date']
    search_fields = ['Operator', 'station', 'Date']
    # list_editable = ['Operator', 'station', 'opc', 'Date']
    list_filter = ['Operator', 'station', 'Date','Operator']
    filter_horizontal = ['Operator', 'station', 'opc']
    class Meta:
        model = Opc_To_Stations
admin.site.register(Opc_To_Stations, Admin_Opc_To_Stations)




class Admin_Tracing_Products(admin.ModelAdmin):
    search_fields = ['station',' order','product','Operator','tracebility_code', 'Date' , 'Time']
    list_display = ['Date' , 'Time']
    # fieldsets =  ('station',' order','product','Operator','tracebility_code', 'Date' , 'Time')
    # filter_horizontal = ['station',' order','product','Operator','tracebility_code', 'Date' , 'Time']
    list_filter = ['station','order','product','Operator','tracebility_code', 'Date' , 'Time']

    class Meta:
        model = Tracing_Products

admin.site.register(Tracing_Products, Admin_Tracing_Products)




class AdminTracebilityData(admin.ModelAdmin):
    # list_display_links =  ['Operator', 'Station', 'Order', 'Product', 'tracebilityCode', 'Date', 'Time']
    list_display =  ['Operator', 'Station', 'Order', 'Product', 'tracebilityCode', 'Date', 'Time']
    # list_select_related = ['Operator', 'Station', 'Order', 'Product', 'tracebilityCode',]

    search_fields = ['Operator', 'Station', 'Order', 'Product', 'tracebilityCode', 'Date']
    list_filter = [ 'Operator', 'Station', 'Order', 'Product', 'Date']
     # = ['Operator', 'Station', 'Order', 'Product', 'tracebilityCode', 'Date', 'Time']
    list_per_page = 1000

    class Meta:
        models = TracebilityData
admin.site.register(TracebilityData, AdminTracebilityData)



class AdminUnknownOperator(admin.ModelAdmin):
    list_display = ['station', 'tracebilityCode', 'Order', 'Product', 'Date', 'Time']

    class Meta:
        models = UnknownOperator
admin.site.register(UnknownOperator, AdminUnknownOperator)


class AdminRepairStation(admin.ModelAdmin):
    list_display  =  ['Operator', 'Station','Description', 'Order', 'Product','Entery', 'Exit','State', 'tracebilityCode', 'Date', 'Time']
    class Meta:
        model = RepairStation
admin.site.register(RepairStation, AdminRepairStation)