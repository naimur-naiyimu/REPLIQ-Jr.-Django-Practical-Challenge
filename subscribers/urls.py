from django.urls import path
from .views import PhoneCompanyList, PhoneCompanyDetail, SubscriberList, SubscriberDetail

urlpatterns = [
    path('phone_companies/', PhoneCompanyList.as_view(), name='phone_company_list'),
    path('phone_companies/<int:pk>/', PhoneCompanyDetail.as_view(),name='phone_company_detail'),
    path('subscribers/', SubscriberList.as_view(), name='subscriber_list'),
    path('subscribers/<int:pk>/', SubscriberDetail.as_view(),name='subscriber_detail'),
]
