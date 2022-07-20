
from xml.etree.ElementInclude import include
from django.urls import path

# from users.views import create_user
from django.urls import path,include

urlpatterns = [
    
    path('',include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls'))
]