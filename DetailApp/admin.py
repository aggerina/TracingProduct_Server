from django.contrib import admin
from DetailApp.forms import FormAppDetail
from DetailApp.models import AppDetail, ClientApp

class AdminAppDetail(admin.ModelAdmin):
    list_display = ['__str__', 'NameApp','version', 'Description', 'Active']

    class Meta:
        model  = AppDetail
admin.site.register(AppDetail, AdminAppDetail)


class AdminClientApp(admin.ModelAdmin):
    form = FormAppDetail
    list_display = ['__str__','name', 'App', 'version', 'Description', 'Active', 'Server_Address', 'send_port', 'DataBase_Address', 'USER_SERVER', 'BarcodeProdocer', 'BarcodeRepair', 'BarcodeRestart', 'BarcodeShutdown']
    class Meta:
        model = ClientApp

admin.site.register(ClientApp, AdminClientApp)