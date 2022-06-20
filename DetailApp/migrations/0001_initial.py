# Generated by Django 3.2.9 on 2021-12-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='عنوان')),
                ('NameApp', models.CharField(blank=True, max_length=150, null=True, verbose_name='نام اپلیکیشن')),
                ('Description', models.TextField(blank=True, null=True, verbose_name='')),
                ('Active', models.BooleanField(blank=True, null=True, verbose_name='فعال')),
            ],
            options={
                'verbose_name': 'توضیحات',
                'verbose_name_plural': 'لیست توضیحات',
            },
        ),
    ]
