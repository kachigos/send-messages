from rest_framework import serializers
from .models import *

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class Freight_brokersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Freight_brokers
        fields = '__all__'

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

# USfuelsystems

class UscontactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsContact
        fields = '__all__'