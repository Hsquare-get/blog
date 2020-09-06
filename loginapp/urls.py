from django.urls import path
from . import views

app_name="loginapp"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot/', views.forgot, name='forgot'),
    path('pwreset/', views.pwreset, name='pwreset'),
]