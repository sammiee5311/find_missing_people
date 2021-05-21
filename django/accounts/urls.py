from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'), # root path
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='check_image'),
]