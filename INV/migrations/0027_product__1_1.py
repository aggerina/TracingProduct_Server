# Generated by Django 3.2.9 on 2022-01-20 11:42

import INV.models
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('INV', '0026_auto_20220120_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='_1_1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=700, size=[600, 700], upload_to=INV.models.upload_image_path),
        ),
    ]
