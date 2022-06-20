# from django.db import models
#
#
# class AppDetail(models.Model):
#     title = models.CharField(max_length=150,blank=True, null=True, verbose_name="عنوان")
#     NameApp = models.CharField(max_length=150, blank=True, null=True, verbose_name="نام اپلیکیشن")
#     Description = models.TextField(blank=True,null=True, verbose_name="")
#     class Meta:
#         verbose_name = "توضیحات"
#         verbose_name_plural = 'لیست توضیحات'
#
#     def __str__(self):
#         return self.title