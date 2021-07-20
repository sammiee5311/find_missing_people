from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'), # root path
    path('map/', views.map, name='map'),
    path('request/', views.request, name='request'),
]
