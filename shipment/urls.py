
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shipment_page, name='shipment_page')
]
