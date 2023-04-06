from django.urls import path
from . import views

urlpatterns = [
    # Device URLs
    path('devices/', views.DeviceList.as_view(), name='device-list'),
    path('companies/<int:company_id>/devices/',views.CompanyDeviceList.as_view(), name='company-device-list'),
    path('devices/checked-out/', views.CheckedOutDevicesList.as_view(),name='checked-out-device-list'),
    path('devices/<int:device_id>/history/',views.DeviceHistoryList.as_view(), name='device-history-list'),
    path('devices/<int:device_id>/check-out/',views.CheckOutDevice.as_view(), name='check-out-device'),
    path('devices/<int:device_id>/return/',views.ReturnDevice.as_view(), name='return-device'),

    # Company URLs
    path('companies/', views.CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', views.CompanyDetail.as_view(), name='company-detail'),
    path('companies/<int:company_id>/employees/',views.CompanyEmployeeList.as_view(), name='company-employee-list'),

    # Employee URLs
    path('employees/', views.EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:employee_id>/checked-out-devices/',views.CheckedOutDevicesByEmployeeList.as_view(), name='checked-out-devices-by-employee'),
]
