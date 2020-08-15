from django.urls import path
from . import views 

urlpatterns = [
    path('login', views.login, name="login"),
    path('registeration', views.registeration, name="registeration"),
    
    path('sucsess', views.success, name="success"),
]

