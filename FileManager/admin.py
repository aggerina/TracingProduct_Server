from django.contrib import admin

from FileManager import models


class AdminSalase(admin.ModelAdmin):
    list_display = ["File", "version", "Description"]
    class Meta:
        model = models.SalesData

admin.site.register(models.SalesData, AdminSalase)
