# Generated by Django 3.2.9 on 2022-02-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRACING', '0026_auto_20220228_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairstation',
            name='tracebilityCode',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='کد ردیابی'),
        ),
        migrations.AlterField(
            model_name='unknownoperator',
            name='Order',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='سفارش'),
        ),
    ]
