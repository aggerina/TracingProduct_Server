


from django.urls import include, path, URLPattern
from rest_framework import routers
from RestApi import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from DetailApp.views import DetailApp
from TRACING.views import HomePageView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('admin/', admin.site.urls, name='AdminDashboard'),
    path('', DetailApp),
    path('Tracing/', include('TRACING.urls')),
    path('auth/', include('TracingAuth.urls')),

    path('rest/', include('RestApi.urls')),
    # path('API_Person/<int:PersonalCode>', views.DetailPerson),
    # path('API_Person/<PersonalCode>', views.DetailPersonal.as_view()),




    path('cli/', include('TRACING.urls')),

    # path('Api/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
