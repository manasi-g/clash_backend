from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('registeration', views.registeration, name="registeration"),
    path('', views.home, name="home"),
    path('success/', views.success, name="success"),
]

