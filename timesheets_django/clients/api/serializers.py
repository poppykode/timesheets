from rest_framework import serializers
from clients.models import Client, Contact 


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('contact','first_name','last_name','office_number','title','mobile_number','email')

class ClientSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)
    class Meta:
        model = Client
        fields = ('id','name','address','contacts',)