from django.urls import path
from .views import *

urlpatterns = [
    # USfuelsystems
    path('USfuelsystems/contact/', UsContactView.as_view()),

    # usdispatch
    path('usdispatch/career/', CareerView.as_view()),
    path('usdispatch/Freight-brokers/', Freight_brokersView.as_view()),
    path('usdispatch/owner/', OwnerView.as_view()),
    path('usdispatch/contact/', ContactView.as_view()),
]