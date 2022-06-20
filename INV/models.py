from enum import unique

from django.db import models
import os, random
from django.db.models import Q
from django_resized import ResizedImageField
#
# from Product_Category.models import Products_category
#

def get_file_name_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27565656665)
    name, ext = get_file_name_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"

    return f"products/{final_name}"

def upload_Instructions_path(instance, filename):
    new_name = random.randint(1, 27565656665)
    name, ext = get_file_name_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"

    return f"Instructions/{final_name}"


class ProductManager(models.Manager):
    def Get_by_id(self, Product_id):
        qs = self.get_queryset().filter(id=Product_id)
        if qs.count() == 1:
            return qs.first()
        return None


class Product_Manager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def Get_by_id(self, Product_id):
        qs = self.get_queryset().filter(id=Product_id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, Query):
        lookup = (Q(title__icontains=Query)
                  | Q(description__contains=Query)
                  | Q(tag__title__icontains=Query)
                  )
        return self.get_queryset().filter(lookup, active=True).distinct()

class Part(models.Model):
    name = models.CharField(null=True, blank=True, max_length=250)
    PartNumber = models.CharField(unique=False, max_length=10,null=True, blank=True, verbose_name='کد محصول')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='عکس قطعه')
    description = models.TextField( blank=True, null=True, verbose_name='توضیحات')
    price = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=3, default=0, verbose_name='قیمت')
    active = models.BooleanField(blank=True,default=True)
    slug = models.SlugField(null=True, blank=True)
    Quantiti  = models.CharField(max_length=3, blank=True,null=True, default=1, verbose_name='تعداد')
    title = models.CharField(null=True, blank=True, max_length=250, verbose_name='عنوان')

    objects = Product_Manager()

    class Meta:
        verbose_name = 'قطعه'
        verbose_name_plural = 'قطعات'

    def __str__(self):
        return f"{str(self.description)}__{str(self.PartNumber)} "

class BOMS(models.Model):
    name = models.CharField(null=True, blank=True, max_length=250)
    PartNumber = models.CharField( max_length=10, null=True, blank=True, verbose_name='کد محصول')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='عکس قطعه')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    price = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=3, default=0, verbose_name='قیمت')
    active = models.BooleanField(blank=True, default=True)
    slug = models.SlugField(null=True, blank=True)
    Quantiti = models.CharField(max_length=3, blank=True, null=True, default=1, verbose_name='تعداد')
    title = models.CharField(null=True, blank=True, max_length=250, verbose_name='عنوان')

    objects = Product_Manager()

    class Meta:
        verbose_name = 'BOM'
        verbose_name_plural = 'BOMS'

    def __str__(self):
        return f"{str(self.description)}__{str(self.PartNumber)} "



class Product(models.Model):
    title = models.CharField(blank=True,null=True, max_length=250, verbose_name='محصول')
    name = models.CharField(blank=True,null=True, max_length=50)
    Product_code = models.CharField(unique=True, blank=True,null=True, max_length=11, verbose_name='کد محصول')
    Tracebility_code = models.CharField(blank=True,null=True,max_length=11, verbose_name='کد ردیابی')
    description = models.TextField(blank=True, default=0,null=True, verbose_name='توضیحات')
    price = models.DecimalField(max_digits=20, decimal_places=3,blank=True,null=True, verbose_name='قیمت')
    active = models.BooleanField(blank=True,default=True, null=True,)
    slug = models.SlugField(blank=True,null=True,)
    # category = models.ManyToManyField(Products_category, blank=True, null=True,  verbose_name='دسته بندی محصولات')
    image = ResizedImageField(size=[300,250], quality=500, upload_to=upload_image_path, null=True, blank=True, verbose_name='عکس محصول')
    # Instructions = models.FileField(upload_to=upload_image_path,null=True,  blank=True, verbose_name='دستورالعمل ساخت ')
    Instructions1 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_image_path,null=True,  blank=True, verbose_name='دستورالعمل ساخت 1')
    Instructions2 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_image_path,null=True,  blank=True, verbose_name='دستورالعمل ساخت 2')

    BOMS = models.ManyToManyField(BOMS, blank=True, verbose_name='BOM')
    Part  = models.ManyToManyField(Part, blank=True, verbose_name='قطعات')
    Quantiti  = models.CharField(max_length=6, blank=True, null=True, default=1, verbose_name='تعداد')

    _1_Placing_01 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_Placing_01 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_Placing_02 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_Placing_02 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_1 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_1 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_2 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_2 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_3 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_3 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_4 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_4 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_5 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_5 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_6 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_6 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_7 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_7 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_8 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_8 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_9 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_9 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_10 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_10 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_11 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_11 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_12 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_12 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_13 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_13 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_LastTest_01 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_LastTest_01 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_LastTest_02 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_LastTest_02 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_LastTest_03 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_LastTest_03 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_LastTest_04 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_LastTest_04 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_LastTest_05 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_LastTest_05 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_Checking = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_Checking = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_Kafchini = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_Kafchini = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_QC_01 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_QC_01 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_QC_02 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_QC_02 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_Boxing_01 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_Boxing_01 = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)

    _2_Repair = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _1_Repair = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)

    _1_IT = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)
    _2_IT = ResizedImageField(size=[600,700], quality=700, upload_to=upload_Instructions_path,null=True,  blank=True)


    objects = Product_Manager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return str(self.description + '__'+ self.Product_code )

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.slug.replace(' ', '-')}"




