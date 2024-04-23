from django.urls import path
from .views import *

urlpatterns = [
    path("transfer/", TransferAPi.as_view())
]