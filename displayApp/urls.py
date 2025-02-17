from django.urls import path
from .views import *


urlpatterns = [
    path('displayProduct',displayProduct,name='display'),
    path('productDetails',productDetails,name='productDetails'),
]
            