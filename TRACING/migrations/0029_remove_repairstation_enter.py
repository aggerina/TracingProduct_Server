# Generated by Django 3.2.9 on 2022-03-03 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TRACING', '0028_auto_20220303_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repairstation',
            name='Enter',
        ),
    ]
