
from django.db import models
from django_jalali.db import models as jmodels
from django_jalali.forms.widgets import  jDateTimeInput
import datetime
import uuid
# from khayyam.jalali_date import JalaliDate
import os , random

from django_resized import ResizedImageField

from INV.models import Product
from Employ.models import Person


def get_file_name_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27565656665)
    name, ext = get_file_name_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"

    return f"products/{final_name}"


class Station(models.Model):
    title = models.CharField(unique=True, blank=False, default='ایستگاه', max_length=20, verbose_name='عنوان')

    StationNumber = models.IntegerField(unique=True, blank=True, null=True )
    Active = models.BooleanField(default=False, verbose_name="فعال")
    Connected  = models.BooleanField(default=False, verbose_name="اتصال شده ")

    class Meta:
        verbose_name = 'ایستگاه'
        verbose_name_plural = 'ایستگاهای کاری '

    def __str__(self):
        return self.title





class Device_Connected(models.Model):
    title = models.CharField(blank=True,null=True, max_length=20, verbose_name='عنوان')
    Operators	= models.ManyToManyField(Person, blank=True,verbose_name='کد پرسنلی')
    # CodeOperator	= models.IntegerField(unique=True, blank=False, default=False ,verbose_name='کد پرسنلی')
    Data            = jmodels.jDateField(blank=True,null=True, verbose_name='روز اتصال')
    time            = models.TimeField(blank=True,null=True, verbose_name='زمان اتصال')
    # time            = models.DateTimeField(default=False,verbose_name='زمان اتصال ایستگاه ')
    # Stationnumber   = models.IntegerField(unique=True, blank=True, null=True, verbose_name='شماره ایستگاه ')
    Stations   = models.ManyToManyField(Station,    verbose_name='شماره ایستگاه ')

    class Meta:
        verbose_name = 'ایستگاه متصل شده '
        verbose_name_plural = 'ایستگاهای متصل شده '

    def __str__(self):
        return self.title


class Construction_processes(models.Model):

    title =  models.CharField(blank=False,max_length=150, null=False , verbose_name="مرحله ساخت ")

    Order =  models.CharField(blank=False,max_length=5, null=False , verbose_name="شماره مرحله ")
    Description =  models.TextField(blank=False, null=False , verbose_name="توضیحات")

    Level =  models.IntegerField( blank=False, null=False , verbose_name="درجه اهمیت کار ")

    # guide = models.FileField(upload_to=upload_image_path,null=True, blank=True,   verbose_name=" دستورالعمل این مرحله ار OPC")

    class Meta:
        verbose_name = "مرحله ساخت "
        verbose_name_plural = "مراحل ساخت "


    def __str__(self):
        return self.title


class OpcDefualt(models.Model):
    title = models.CharField(blank=True,null=True,  max_length=150, verbose_name="عنوان OPC ")
    ConstructionProcesses = models.ManyToManyField(Construction_processes, verbose_name="دستور ساخت ")


    class Meta:
        verbose_name = "دستور ساخت "
        verbose_name_plural = "دستور ساخت ها "

    def __str__(self):
        return self.title



class Opc_To_Stations(models.Model):
    title = models.CharField(blank=False, max_length=150, null=False, verbose_name="عنوان")
    # Order = models.ManyToManyField(Orders, blank=True, verbose_name="سفارش")
    Operator = models.ManyToManyField(Person, verbose_name="پرسنل")
    station = models.ManyToManyField(Station, verbose_name="ایستگاه کاری")
    # opc = models.ManyToManyField(OpcDefualt, verbose_name="دستور ساخت ")
    opc = models.ManyToManyField(Construction_processes, verbose_name="دستور ساخت ")
    # opc = models.FileField(upload_to=upload_image_path,blank=True, null=True, verbose_name="دستور ساخت ")
    Instructions1 = ResizedImageField(size=[600, 700], quality=700, upload_to=upload_image_path, null=True,
                                      blank=True, verbose_name='دستورالعمل ساخت 1')
    Instructions2 = ResizedImageField(size=[600, 700], quality=700, upload_to=upload_image_path, null=True,
                                      blank=True, verbose_name='دستورالعمل ساخت 2')


    Date = jmodels.jDateTimeField(blank=True, null=True, verbose_name="زمان و تاریخ")

    def get_parents(self):
        return ",".join([str(p) for p in self.parent.all()])

    def __unicode__(self):
        return "{0}".format(self.title)

    class Meta:
        verbose_name = " ثبت دستورساخت ها نسبت به هر استگاه "
        verbose_name_plural = "جدول ثبت دستورساخت ها نسبت به هر استگاه"

    def __str__(self):
        return self.title


class Orders(models.Model):
    title = models.CharField(blank=True, null=True,  max_length=100, verbose_name='عنوان')
    code = models.CharField(unique=True, blank=False ,null=True, max_length=20, verbose_name='کد سفارش ')
    Recive_Data = jmodels.jDateField(blank=True, null=True, verbose_name="زمان دریافت سفارش")
    Count = models.IntegerField(blank=True, null=True, verbose_name="تعداد سفارش")
    # Recive_Data = models.DateTimeField(blank=False, default=False, verbose_name="زمان دریافت سفارش")
    # MaximumTime = models.DateTimeField(blank=True, default=False, verbose_name='حد اکثر تاریخ تولید ')
    MaximumTime = jmodels.jDateField(blank=True,null=True ,verbose_name='حد اکثر تاریخ تولید ')
    Product    = models.ManyToManyField(Product)
    opc_To_stations = models.ManyToManyField(Opc_To_Stations, verbose_name="دستور ساخت و استگاه ")



    class Meta:
        verbose_name = 'سفارش '
        verbose_name_plural = 'سفارش های فعال'


    def __str__(self):
        return self.title



class Opc_Product(models.Model):
    title = models.CharField(blank=False,default='عنوان', max_length=20, verbose_name='عنوان')
    Product = models.ManyToManyField(Product,blank=False, verbose_name=' محصول ')
    Opc_Order    = models.FileField(upload_to=upload_image_path, null=True, blank=True, verbose_name='فایل مدیریت پرسنل')
    Order_code_Product  = models.ManyToManyField(Orders, blank=False, verbose_name=' OPC مربوط به کد سفارش ')
    Instructions = models.FileField(upload_to=upload_image_path,null=True,  blank=False, verbose_name='دستورالعمل ساخت ')
    picture  = models.ImageField( upload_to=upload_image_path, null=True, blank=False, verbose_name='عکس محصول')
    time = jmodels.jDateField(null=True,blank=True,  verbose_name="روز ثبت ")
    date = models.TimeField(null=True,blank=True,  verbose_name="زمان ثبت ")


    class Meta:
        verbose_name = 'OPC'
        verbose_name_plural = 'فرایندها'

    def __str__(self):
        return self.title




class Recipt_out(models.Model):
    # title = models.CharField(blank=False,default='عنوان',max_length=20, verbose_name='عنوان')
    cod_product         = models.CharField(blank=True,null=True,max_length=100,  verbose_name='کد محصول ')
    description_prodact = models.TextField(max_length=250,blank=True, null=True,  verbose_name='شرح قطعه')
    code_Tracebility    = models.IntegerField(blank=False,default=True, verbose_name='کد ردیابی' )
    Qountiti            = models.IntegerField(blank=True, null=True,  verbose_name='تعداد')
    order_code          = models.IntegerField(blank=True, null=True,  verbose_name='کد سفارش ')
    curent_data         = models.CharField(max_length=20, blank=True, null=True,  verbose_name='تاریخ ')
    Cod_Operator        = models.CharField(max_length=12, blank=True, null=True,  verbose_name='کد اپراتور')
    destinastion_store  = models.CharField(blank=True, null=True, max_length=70,  verbose_name='انبار مقصد')
    sorce_store        = models.CharField(blank=True, null=True, max_length=70,  verbose_name='انبار مبدا')
    form_number        = models.CharField(blank=True, null=True,max_length=10,  verbose_name='شماره حواله')
    position_out        = models.CharField(blank=True, null=True, max_length=50,  verbose_name='نوع خروج')
    center_cost        = models.CharField(blank=True, null=True, max_length=70,  verbose_name='مرکز هزینه ')


    class Meta:
        verbose_name = 'حواله خروج'
        verbose_name_plural = 'حواله های  خروج'

    def __str__(self):
        return self.cod_product




class Sum_Recipt_out(models.Model):
    # title = models.CharField(blank=False, default='عنوان', max_length=20, verbose_name='عنوان')
    product_cod_SUM = models.CharField(blank=True, max_length=10, verbose_name='کد  محصول ')
    DESCRIPTION     = models.CharField(blank=True, max_length=200, verbose_name='شرح')
    Sum_all_Pro     = models.IntegerField(blank=True, verbose_name='جمع کل')
    order_cod     = models.IntegerField(blank=True ,verbose_name='کد سفارش')
    # form_number = models.OneToOneField(Recipt_out, on_delete=models.CASCADE, primary_key=True, verbose_name='شماره فرم')
    form_number = models.IntegerField(blank=False, default=0,  verbose_name='شماره حواله')

    class Meta:
        verbose_name = 'جمع حواله خروج'
        verbose_name_plural = ' جمع حواله های  خروج'

    # def __str__(self):
    #     return self.title


class TracebilityCode(models.Model):
    # title = models.CharField(blank=False, default='عنوان', max_length=20, verbose_name='عنوان')

    Tracebility_code = models.CharField(unique=True, max_length=30, null=True, blank=True, verbose_name='کد ردیابی')
    Date             = jmodels.jDateField(blank=True,null=True, verbose_name='تاریخ')
    time = models.TimeField(blank=True, null=True)
    order = models.ManyToManyField(Orders, blank=True, verbose_name=" سفارش")
    # Date             = models.DateTimeField(blank=True, verbose_name='تاریخ')




    class Meta:
        verbose_name = 'کد های ردیابی تولید شده '
        verbose_name_plural = ' جدول کد های ردیابی تولید شده'

    def __str__(self):
        return self.Tracebility_code




class Station_to_order(models.Model):
    # title = models.CharField(blank=False, default='عنوان', max_length=30, verbose_name='عنوان')
    StationNumber = models.ManyToManyField(Station, blank=False, default=0)
    order = models.ManyToManyField(Orders, blank=False, default=0)
    person = models.ManyToManyField(Person, blank=False, default=0)
    Time_for_work = jmodels.jDateTimeField(blank=True,null=True,verbose_name="تاریخ شروع شفارس در خط تولید ")


    class Meta:
        verbose_name = "اتصال ایستگاه و پرسنل به سفارش"
        verbose_name_plural = 'اتصال ایستگاه و پرسنل به سفارش'
    #

    def __str__(self):
        return self.StationNumber






class Tracing_Products(models.Model):
    Operator= models.ManyToManyField(Person, verbose_name="اپراتور")
    station = models.ManyToManyField(Station, verbose_name='ایستگاه')
    order   = models.ManyToManyField(Orders, verbose_name="سفارش")
    product = models.ManyToManyField(Product, verbose_name="محصول")
    tracebility_code  = models.ManyToManyField(TracebilityCode, verbose_name="کد ردیابی")
    Date = jmodels.jDateField(null=False, blank=False, default=0, verbose_name="تاریخ روز ")
    Time  = models.TimeField(null=False, blank=False, default=0, verbose_name="زمان")
    class Meta:
        verbose_name = " ردیابی قطعات "
        verbose_name_plural = " جدول ردیابی قطعات   "

    def __str__(self):
        return self.Operator + self.station


class TracebilityData(models.Model):
    Operator  = models.CharField(max_length=40, blank=True, verbose_name="اپراتور")
    Station = models.CharField(max_length=40, blank=True, verbose_name="ایسنگاه")
    Order = models.CharField(max_length=40, blank=True, verbose_name="سفارش")
    Product = models.CharField(max_length=40, blank=True, verbose_name="محصول")
    tracebilityCode = models.CharField(max_length=40, blank=True,  verbose_name="کد ردیابی")
    Date =   jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ')
    Time = models.TimeField(blank=True, null=True, verbose_name='زمان')

    # Operator  = models.ManyToManyField(Person, blank=True, verbose_name="اپراتور")
    # Station = models.ManyToManyField(Station, blank=True, verbose_name="ایسنگاه")
    # Order = models.ManyToManyField(Orders, blank=True, verbose_name="سفارش")
    # Product = models.ManyToManyField(Product, blank=True, verbose_name="محصول")
    # tracebilityCode = models.ManyToManyField(TracebilityCode, blank=True,  verbose_name="کد ردیابی")
    # Date =   jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ')
    # Time = models.TimeField(blank=True, null=True, verbose_name='زمان')
    class Meta:
        verbose_name = " ردیابی کد "
        verbose_name_plural = " جدول ردیابی کد های    "

    def __str__(self):
        return str(self.tracebilityCode)




class TracebilityData_2(models.Model):
    Operator  = models.CharField(max_length=40, blank=True, verbose_name="اپراتور")
    Station = models.CharField(max_length=40, blank=True, verbose_name="ایسنگاه")
    Order = models.CharField(max_length=40, blank=True, verbose_name="سفارش")
    Product = models.CharField(max_length=40, blank=True, verbose_name="محصول")
    tracebilityCode = models.CharField(max_length=40, blank=True,  verbose_name="کد ردیابی")
    Date =   jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ')
    Time = models.TimeField(blank=True, null=True, verbose_name='زمان')

    # Operator  = models.ManyToManyField(Person, blank=True, verbose_name="اپراتور")
    # Station = models.ManyToManyField(Station, blank=True, verbose_name="ایسنگاه")
    # Order = models.ManyToManyField(Orders, blank=True, verbose_name="سفارش")
    # Product = models.ManyToManyField(Product, blank=True, verbose_name="محصول")
    # tracebilityCode = models.ManyToManyField(TracebilityCode, blank=True,  verbose_name="کد ردیابی")
    # Date =   jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ')
    # Time = models.TimeField(blank=True, null=True, verbose_name='زمان')
    class Meta:
        verbose_name = " کد ردیابی ذخیره شده "
        verbose_name_plural = " جدول ردیابی کد های ذخیره شده  "

    def __str__(self):
        return str(self.tracebilityCode)


class UnknownOperator(models.Model):
    station = models.CharField(blank=True, max_length=20, null=True, verbose_name='ایستگاه')
    tracebilityCode = models.CharField(blank=True, max_length=20 , null=True, verbose_name="کد ردیابی")
    Order = models.CharField(max_length=40,null=True, blank=True, verbose_name="سفارش")
    Product = models.CharField(max_length=40, blank=True,  verbose_name="محصول")
    Date =   jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ')
    Time = models.TimeField(blank=True, null=True, verbose_name='زمان')

    class Meta:
        verbose_name=  'اپراتور ناشناخته'
        verbose_name_plural = ' جدول اپراتور های  ناشناخته '

    def __str__(self):
        return self.tracebilityCode


class RepairStation(models.Model):
    Operator  = models.CharField(max_length=40, null=True, blank=True, verbose_name="اپراتور")
    Station = models.CharField(max_length=40, null=True, blank=True, verbose_name="ایسنگاه")
    Order = models.CharField(max_length=40, null=True, blank=True, verbose_name="سفارش")
    Description =  models.CharField(max_length=40, null=True, blank=True, verbose_name="توضیحات")
    Entery = models.CharField(max_length=40,null=True, blank=True, verbose_name="ورودی های ایستگاه تعمیرات ")
    Exit = models.CharField(max_length=40, null=True, blank=True )
    State = models.CharField(max_length=20, null=True, blank=True )
    Cuase = models.CharField(max_length=260, null=True, blank=True )
    Product = models.CharField(max_length=40, null=True, blank=True, verbose_name="محصول")
    tracebilityCode = models.CharField(max_length=40, null=True, blank=True,   verbose_name="کد ردیابی")
    Date =   jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ')
    Time = models.TimeField(blank=True, null=True, verbose_name='زمان')

    class Meta:
        verbose_name = "تعمیرات"
        verbose_name_plural = " جدول محصولات تعمیر شده"

    def __str__(self):
        return str(self.tracebilityCode)




