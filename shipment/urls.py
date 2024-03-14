
from django.urls import path
from . import views

app_name = 'shipment'

urlpatterns = [
    path('', views.shipment_page, name='shipment_page')
]
