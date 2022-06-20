from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import FormView, BaseDetailView
from django.views.generic.base import TemplateView

from DetailApp.models import AppDetail
from TRACING.forms import FormBarcodeGenerator
from Employ.models import Person
from TRACING.models import TracebilityCode
from TRACING.forms import *
from TRACING.models import Orders
import shortuuid
import datetime
from khayyam import jalali_date



def HomePageView(request):
    if request.user.is_authenticated:
        context = {
            "appDetail": AppDetail.objects.all()
        }
        return render(request, "AdminPanel/index.html", context)

    return  redirect('LoginePage')


# class HomePageView(TemplateView):
#     # if request.user.is_authenticated:
#
#     template_name = "AdminPanel/index.html"
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['AppDetailes'] = AppDetail.objects.all()
#         return context
#     # redirect('LoginePage')
#


# class BarcodeGenerator(FormView):
#     template_name = 'AdminPanel/BarcodeGenerator.html'
#     form_class = Tracebility_codeGenerateForm
#     def form_valid(self, form):
#         pass
#
# #

class ExportBarcode(ListView):
    print(jalali_date)
    model = TracebilityCode
    template_name =  'AdminPanel/BarCodeExport.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = "-"
        object_list  = TracebilityCode.objects.filter(Date=str(jalali_date.JalaliDate().today()), order__code__contains=query)
        return object_list

def BarcodeManager(request):
    context = {}
    BarcodeForm = FormBarcodeGenerator(request.POST or None)
    if request.user.is_authenticated:


        if BarcodeForm.is_valid():
            if request.method == 'POST':

                countBarcode = BarcodeForm.cleaned_data.get('CountBarcode')
                orderCode = BarcodeForm.cleaned_data.get('OrderCode')
                ORDER = Orders.objects.get(code=orderCode)
                for barcode in range(int(countBarcode)):
                    tracebilityCode = TracebilityCode.objects.create(Tracebility_code=shortuuid.uuid()[:8],  Date=datetime.date.today(), time= datetime.datetime.now())
                    tracebilityCode.order.add(ORDER)

                    # tracebilityCode.order = orderCode
                    # tracebilityCode.order = orderCode
                    # tracebilityCode.Tracebility_code = shortuuid.uuid()[:10]
                    tracebilityCode.save()









        context = {
            'title':"Barcode Generator",
            "BarcodeForm": BarcodeForm,
            "TracebilityCode" :  TracebilityCode.objects.filter().all()
        }

        return render(request, 'AdminPanel/BarcodeGenerator.html', context)
    return redirect("LoginePage")


# class ProfilePage(TemplateView):
#
#     template_name = "AdminPanel/profile.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Person'] = Person.objects.all()
#         return context

def ProfilePage(request):
    if request.user.is_authenticated:
        context = {
            "Person": Person.objects.all()
        }
        return render(request, "AdminPanel/profile.html", context)

    return  redirect('LoginePage')
