from django.db import models
import os
def get_file_name_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_App_path(instance, filename):

    name, ext = get_file_name_ext(filename)
    final_name = f"{instance.id}-{instance.name}{ext}"

    return f"Files_Sales/{final_name}"

class SalesData(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name="نام ")
    File  = models.FileField(upload_to=upload_App_path, blank=True, null=True , verbose_name="File")
    version = models.FloatField(blank=True, null=True, verbose_name='ورژن')
    Description = models.TextField(blank=True, null=True, verbose_name="توضیحات")


    # def __str__(self):
    #     return self.name
