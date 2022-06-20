from django.db import models


class Products_category(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    name  = models.CharField(max_length=150, verbose_name='نام در url')

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته ها '

    def __str__(self):
        return self.title