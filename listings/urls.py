from django.urls import path

from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.listings_all, name='listings_all'),
    path('<int:listing_id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]
