from TRACING.models import TracebilityCode
from django.forms import ModelForm
from django import forms
from TRACING.models import  Orders
from django_jalali import forms as Jform
# class Tracebility_codeGenerateForm(ModelForm):
#     class Meta:
#         model = TracebilityCode
#         fields = [ 'Date', 'order']



class FormBarcodeGenerator(forms.Form):
    CountBarcode = forms.CharField(
        widget=forms.TextInput(attrs={'id':'CountBarcode','placeholder':'لطفا تعداد بارکد ها را وارد کنید ','class':'form-control'}),
        label=' تعداد کد سفارش ')
    OrderCode = forms.CharField(
        widget=forms.TextInput(attrs={'id':'OrderCode', 'placeholder':'لطفا کد سفارش را وارد کنید','class':'form-control'}),
        label='کد سفارش')

    def clean_OrderCode(self):
        orderCode = self.cleaned_data.get('OrderCode')


        is_exists_Order = Orders.objects.filter(code=orderCode).exists()
        if not  is_exists_Order:
            raise forms.ValidationError('کد سفارش وارد شده در دیتابیس وجود ندارد')

        return orderCode

# class FormBarcodeExport(forms.Form):
#     JDateFields = Jform.jDateField( widget=forms.e(attrs={'id':'JDateField'}))
#     def clean_JDateFields(self):
#         jdateField = self.cleaned_data.get('JDateField')
#         # is_exsist_jdate =
