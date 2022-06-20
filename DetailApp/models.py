from django.db import models
import os , random
def get_file_name_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_App_path(instance, filename):

    name, ext = get_file_name_ext(filename)
    final_name = f"{instance.id}-{instance.name}{ext}"

    return f"Applications/{final_name}"



class AppDetail(models.Model):
    title = models.CharField(max_length=150,blank=True, null=True, verbose_name="عنوان")
    NameApp = models.CharField(max_length=150, blank=True, null=True, verbose_name="نام اپلیکیشن")
    Description = models.TextField(blank=True,null=True, verbose_name="توضیحات")
    version = models.IntegerField(blank=True,null=True, verbose_name='ورژن ')
    Active  = models.BooleanField(blank=True, null=True, verbose_name='فعال')
    class Meta:
        verbose_name = "توضیحات"
        verbose_name_plural = 'لیست توضیحات'

    def __str__(self):
        return self.title


class ClientApp(models.Model):

    name = models.CharField(max_length=30, blank=True, null=True, verbose_name="نام اپلیکشن ")
    App = models.FileField(upload_to=upload_App_path, blank=True, null=True, verbose_name="فایل نرم افزار کلاینت ردیابی")
    version = models.FloatField(blank=True, null=True, verbose_name='ورژن')
    Description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    Active = models.BooleanField(blank=True, null=True, verbose_name='فعال')
    Server_Address = models.GenericIPAddressField(blank=False, null=False, default='192.168.4.50')
    send_port = models.CharField(max_length=6, default='8000', verbose_name='PortServer')
    DataBase_Address = models.GenericIPAddressField(blank=False, null=False, default='192.168.4.51')
    DataBase_Name = models.CharField(max_length=20, blank=False, null=False, default='photon')
    DatabasePort = models.CharField(max_length=6, blank=False, null=False, default='5432')
    PASSWORD_SERVER = models.CharField(max_length=50, blank=False, null=False, default='aezakmiHESOYAMFu$!on-123')
    USER_SERVER = models.CharField(max_length=50, blank=False, null=False, default='shaho')
    BarcodeRestart = models.CharField(max_length=12, blank=False, null=False, default='5465406611')
    BarcodeShutdown = models.CharField(max_length=12, blank=False, null=False, default='1254687900')
    BarcodeProdocer = models.CharField(max_length=12, blank=False, null=False, default='5554687910')
    BarcodeRepair = models.CharField(max_length=12, blank=False, null=False, default='7654687920')


    def __str__(self):
        return self.name


# class AppSetting(models.Model):
#     Server_Address = models.IPAddressField(blank=False, null=False, default='192.168.4.50')
#     send_port = models.CharField(max_length=6, verbose_name='PortServer')





