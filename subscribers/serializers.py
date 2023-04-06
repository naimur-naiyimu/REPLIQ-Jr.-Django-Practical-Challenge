from rest_framework import serializers
from .models import PhoneCompany, Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['phone_number', 'company']


class PhoneCompanySerializer(serializers.ModelSerializer):
    subscribers = SubscriberSerializer(many=True, read_only=True)

    class Meta:
        model = PhoneCompany
        fields = ['id', 'name', 'subscribers']
