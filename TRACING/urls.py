from django.urls import path
from TRACING.views import BarcodeManager,HomePageView,ProfilePage, ExportBarcode


urlpatterns = [

    path('BarcodeManager/', BarcodeManager  , name='BarcodeManager'),
    path('ExportBarcode/', ExportBarcode.as_view()  , name='BarcodeExport'),
    path('HomePage/', HomePageView , name='DashboardMain' ),
    path('Profile/', ProfilePage , name='DashboardProfile' ),



]