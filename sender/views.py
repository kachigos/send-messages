from rest_framework import generics

from .serializers import *
from .utils import *

class CareerView(generics.CreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = request.data
        message_text = "Career:\n"
        for key, value in data.items():
            if key in ["username", "dba", 'address', 'apartment', 'city', 'state', 'zip', 'country',
                       'email', 'phone', 'usdot', 'mc', 'ssn', 'number_of_drivers', 'number_of_truck',
                       'type_of_equipment', 'factor_invoices', 'desc', 'choice_file']:
                message_text += f"{key}: {value}\n"
        usdispatch_send_telegram_message(message_text)
        return response

class Freight_brokersView(generics.CreateAPIView):
    queryset = Freight_brokers.objects.all()
    serializer_class = Freight_brokersSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = request.data
        message_text = "Freight brokers:\n"
        for key, value in data.items():
            if key in ["username", "phone", 'email', 'lane', 'budget']:
                message_text += f"{key}: {value}\n"
        usdispatch_send_telegram_message(message_text)
        return response

class OwnerView(generics.CreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = request.data
        message_text = "Owner:\n"
        for key, value in data.items():
            if key in ["username", "phone", 'email', 'dry_van', 'reefer', 'flatbed', 'box_truck', 'number_of_truck']:
                message_text += f"{key}: {value}\n"
        usdispatch_send_telegram_message(message_text)
        return response

class ContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = request.data
        message_text = "Contact:\n"
        for key, value in data.items():
            if key in ["username", "email", 'subject', 'message']:
                message_text += f"{key}: {value}\n"
        usdispatch_send_telegram_message(message_text)
        return response

# USfuelsystems

class UsContactView(generics.CreateAPIView):
    queryset = UsContact.objects.all()
    serializer_class = UscontactSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = request.data
        message_text = "Контакты:\n"
        for key, value in data.items():
            if key in ["username", "phone"]:
                message_text += f"{key}: {value}\n"
        usfuelsystems_send_telegram_message(message_text)
        return response
