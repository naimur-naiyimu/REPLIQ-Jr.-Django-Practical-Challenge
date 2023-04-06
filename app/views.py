from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Company, Device, Employee, DeviceHistory
from .serializers import CompanySerializer, DeviceSerializer, EmployeeSerializer, DeviceHistorySerializer

# views to list all devices
class DeviceList(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

# View to list all devices belonging to a specific company
class CompanyDeviceList(generics.ListAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return Device.objects.filter(company_id=company_id)

# View to list all devices currently checked out by employees
class CheckedOutDevicesList(generics.ListAPIView):
    queryset = Device.objects.filter(status='Checked Out')
    serializer_class = DeviceSerializer

# View to list history of a specific device
class DeviceHistoryList(generics.ListAPIView):
    serializer_class = DeviceHistorySerializer

    def get_queryset(self):
        device_id = self.kwargs['device_id']
        return DeviceHistory.objects.filter(device_id=device_id)

# View to list all companies
class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# View to retrieve details of a specific company
class CompanyDetail(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# View to list all employees
class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# View to list all employees belonging to a specific company
class CompanyEmployeeList(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return Employee.objects.filter(company_id=company_id)

# View to list all devices currently checked out by a specific employee
class CheckedOutDevicesByEmployeeList(generics.ListAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        employee_id = self.kwargs['employee_id']
        return Device.objects.filter(status='Checked Out', checked_out_by_id=employee_id)

# View to check out a device
class CheckOutDevice(generics.UpdateAPIView):
    serializer_class = DeviceSerializer

    def patch(self, request, *args, **kwargs):
        device = get_object_or_404(Device, id=kwargs['device_id'])
        employee = get_object_or_404(Employee, id=request.data['employee_id'])
        device.status = 'Checked Out'
        device.checked_out_by = employee
        device.save()
        return Response(self.get_serializer(device).data)

# View to return a device
class ReturnDevice(generics.UpdateAPIView):
    serializer_class = DeviceSerializer

    def patch(self, request, *args, **kwargs):
        device = get_object_or_404(Device, id=kwargs['device_id'])
        device.status = 'Available'
        device.checked_out_by = None
        device.save()
        return Response(self.get_serializer(device).data)
