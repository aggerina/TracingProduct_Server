from django.shortcuts import render



from django.shortcuts import render, redirect
from TracingAuth.forms import Login_Form, Register_Model

from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.models import User

def login_page(request):
    if request.user.is_authenticated:
        return redirect('DashboardMain')

    Login_Page = Login_Form(request.POST or None)

    if Login_Page.is_valid():
        user_name = Login_Page.cleaned_data.get("user_name")
        password = Login_Page.cleaned_data.get("password")
        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            login(request, user)
            return redirect('DashboardMain')
        else:
            Login_Page.add_error('user_name','کاربری با مشخصات وارد شده وجود ندارد ')



    context = {
        "login_form": Login_Page
    }
    return render(request, "AdminPanel/login.html", context)

def register_page(request):
    if request.user.is_authenticated:
        return redirect('DashboardMain')

    Register_Form =Register_Model(request.POST or None)

    if Register_Form.is_valid():
        user_name = Register_Form.cleaned_data.get("user_namee")
        password = Register_Form.cleaned_data.get("password")
        email = Register_Form.cleaned_data.get("email")
        # user = authenticate(request, username=user_name, password=password)
        User.objects.create_user(username=user_name, email=email, password=password)
        return redirect('LoginePage')

    context = {
        'Register_form': Register_Form
    }
    return render(request, 'AdminPanel/register.html', context)














# class LoginPage(TemplateView):
#
#     template_name = "AdminPanel/login.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Person'] = Person.objects.all()
#         return context
#
#
# class RegisterPage(TemplateView):
#     template_name = "AdminPanel/register.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Person'] = Person.objects.all()
#         return context
