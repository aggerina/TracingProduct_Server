# Generated by Django 3.2.9 on 2022-01-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRACING', '0013_auto_20220115_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipt_out',
            name='Cod_Operator',
            field=models.IntegerField(blank=True, null=True, verbose_name='کد اپراتور'),
        ),
        migrations.AlterField(
            model_name='recipt_out',
            name='Qountiti',
            field=models.IntegerField(blank=True, null=True, verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='recipt_out',
            name='center_cost',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='مرکز هزینه '),
        ),
        migrations.AlterField(
            model_name='recipt_out',
            name='cod_product',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='کد محصول '),
        ),
        migrations.AlterField(
            model_name='recipt_out',
            name='curent_data',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ '),
        ),
        migrations.AlterField(
            model_name='recipt_out',
            name='description_prodact',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='شرح قطعه'),
        ),
        migrations.AlterField(
            model_name='recipt_out',
            name='destinastion_store',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='انبار مقصد'),
        ),
        migrations.AlterField(
            model_name='recipt_out',
            name='form_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='شماره حواله'),
        ),
        migrations.AlterField(
            model_name='recipt_out',
            name='order_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='کد سفارش '),
        ),
        migrations.AlterField(
            model_name='recipt_out',
            name='position_out',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='نوع خروج'),
        ),
        migrations.AlterField(
            model_name='recipt_out',
            name='sorce_store',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='انبار مبدا'),
        ),
    ]
