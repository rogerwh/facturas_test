from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^empresa/(?P<id>[\d{1,9}]+)$', factura_empresa, name="factura_empresa"),
]