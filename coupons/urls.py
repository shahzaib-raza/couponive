from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/<slug:slug>/', views.store_detail, name='store_detail'),
]