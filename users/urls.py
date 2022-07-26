
from django.urls import path, include
from users.views import index_balance
urlpatterns = [
    path('register/', include('dj_rest_auth.registration.urls')),
    path('profile/',index_balance,name='profile'),
]
