from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop),
    path('jeju_olle/', views.jejuolle),
    # path('store_show/', views.Storeshow),
]