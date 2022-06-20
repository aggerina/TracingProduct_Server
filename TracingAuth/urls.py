from django.urls import path
from TracingAuth.views import login_page, register_page


urlpatterns = [

path('login/', login_page , name='LoginePage' ),
path('register/', register_page , name='registerPage' ),

]
