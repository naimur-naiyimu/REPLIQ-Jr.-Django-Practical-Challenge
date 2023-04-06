from rest_framework import generics
from .models import PhoneCompany, Subscriber
from .serializers import PhoneCompanySerializer, SubscriberSerializer


class PhoneCompanyList(generics.ListCreateAPIView):
    queryset = PhoneCompany.objects.all()
    serializer_class = PhoneCompanySerializer


class PhoneCompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneCompany.objects.all()
    serializer_class = PhoneCompanySerializer


class SubscriberList(generics.ListCreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class SubscriberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
