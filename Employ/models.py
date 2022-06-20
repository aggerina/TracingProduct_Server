from django.db import models
import os , random
from django_resized import ResizedImageField
def get_file_name_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27565656665)
    name, ext = get_file_name_ext(filename)
    final_name = f"{instance.id}-{instance.CodeOperator}{ext}"

    return f"Person/{final_name}"

class Organizational_chart(models.Model):
    title  = models.CharField(blank=False, default='عنوان', max_length=20, verbose_name='عنوان')
    name  = models.CharField(blank=True , max_length=30, verbose_name='نام ')
    level = models.IntegerField(blank=False, default=0)

    # person = models.ManyToManyField(Person, verbose_name="پرسنل")

    class Meta:
        verbose_name = "چارت سازمانی "
        verbose_name_plural = "  چارت سازمانی پرسنل ها"


    def __str__(self):
        return self.title




class Person(models.Model):
    title = models.CharField(blank=False, default='عنوان', max_length=20, verbose_name='عنوان')
    Name = models.CharField(blank=False, max_length=30,   verbose_name="نام ")
    LastName = models.CharField(blank=False, max_length=50,   verbose_name="نام خانوادگی")
    # FullName = str(Name) + (LastName)
    Age = models.CharField(blank=True, max_length=5,   verbose_name="سن")
    TelephonNumber = models.CharField(default=0,blank=True, max_length=20,   verbose_name="شماره تلفن")
    Address = models.TextField(blank=True,   verbose_name="ادرس")
    CodeOperator = models.IntegerField(unique=True,blank=False,  verbose_name="کد پرسنلی")
    OrChart =  models.ManyToManyField(Organizational_chart, verbose_name='چارت سازمانی ')
    StartBarcode  = models.CharField(unique=True,max_length=7, default=1,  blank=False,  verbose_name="کد شروع")
    StopBarcode  = models.CharField(unique=True,max_length=7, default=0, blank=False,  verbose_name="کد  پایان")
    Image = ResizedImageField(size=[100,120],quality=200,  upload_to=upload_image_path, null=True, blank=False, verbose_name='عکس پرسنل ')
    Start = models.BooleanField(null=True,blank=True, verbose_name="وضعیت فعال")
    class Meta:
        verbose_name = "پرسنل"
        verbose_name_plural = "پرسنل ها"
    def __str__(self):
        return self.Name +" " + self.LastName







