from rest_framework.serializers import ModelSerializer

from .models import Company, Contact


class CompaniesSerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"


class ContactSheduleSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = ["name", "phone_number"]


class ContactCreateSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"
    
    def create(self, validated_data):
        contact = Contact.objects.create(**validated_data)
        return contact