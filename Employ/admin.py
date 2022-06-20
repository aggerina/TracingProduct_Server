from django.contrib import admin
from .models import  Person , Organizational_chart

class AdminChartsOR(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ['__str__']
    class Meta:
        model = Organizational_chart

admin.site.register(Organizational_chart, AdminChartsOR)


class AdminPerson(admin.ModelAdmin):
    list_display =  ('Name', 'LastName', 'Age', 'TelephonNumber','StartBarcode','StopBarcode', 'Address', 'CodeOperator', 'Image', "Start")
    search_fields = ['Name', 'LastName', 'Age', 'CodeOperator', 'TelephonNumber', 'StartBarcode', 'StopBarcode']
    # list_filter =  ( 'LastName', )
    class Meta:
        model = Person
admin.site.register(Person, AdminPerson)