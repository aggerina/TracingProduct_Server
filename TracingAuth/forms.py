from  django import  forms
from django.contrib.auth.models import User
from django.core import  validators
class Login_Form(forms.Form):

    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام خود را وارد کنید','class':'form-control' }),
        label='نام کاربری')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا پسورد خود را وارد کنید ' , 'class':'form-control'}),
        label='کلمه عبور'

    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user = User.objects.filter(username=user_name).exists()
        if  not is_exists_user:
            raise  forms.ValidationError('کاربری با مشخصات وارد شده ثبت نام نکرده است ')
        return user_name

class Register_Model(forms.Form):

    user_namee = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام خود را وارد کنید' ,'class':'form-control'}),
        label='نام کاربری',
        validators=[
            validators.MaxLengthValidator(limit_value=20,message='تعداد کاراکترهای وارد شده نمیتواند بیشتر از 20 باشد'),
            validators.MinLengthValidator(4,'تعداد کاراکترها از 8 عدد نمیتواند کمتر باشد  '),
        ]
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفاایمیل  خود را وارد کنید', 'class':'form-control'}),
        label='ایمیل',
        validators=[
        validators.EmailValidator('ایمیل وارد شده معتبر نمیباشد '),
            ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا پسورد خود را وارد کنید ' ,'class':'form-control'}),
        label='کلمه عبور'

    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا تکرار  پسورد خود را وارد کنید ', 'class':'form-control'}),
        label=' تکرار   کلمه عبور'

    )
    def clean_email(self):
        email = self.cleaned_data.get('email')

        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('ایمیل وارد شده تکراری میباشد')
        return email


    def clean_user_namee(self):
        user_name = self.cleaned_data.get('user_namee')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()
        if is_exists_user_by_username:
            raise forms.ValidationError('کاربری با این نام وجود دارد ')
        return user_name

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password =  self.cleaned_data.get('re_password')

        if password != re_password:
            raise  forms.ValidationError('پسورد هم خوانی ندارد ')
        return password