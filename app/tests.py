from django.test import TestCase
from django.utils import timezone
from .models import Company, Employee, Device, DeviceHistory

# Company Model Tests
class CompanyModelTests(TestCase):
    def test_company_name_max_length(self):
        company = Company(name='A' * 256)
        with self.assertRaises(Exception):
            company.full_clean()

    def test_company_str(self):
        company = Company(name='abc company limt')
        self.assertEqual(str(company), 'abc company limt')

# Employee Model Tests
class EmployeeModelTests(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='abc company limt')

    def test_employee_str(self):
        employee = Employee(company=self.company, name='Donal Tamp')
        self.assertEqual(str(employee), 'Donal Tamp')

# Device Model Tests
class DeviceModelTests(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='abc company limt')
        self.employee = Employee.objects.create(
            company=self.company, name='Donal Tamp')
        self.device = Device.objects.create(
            company=self.company, make='Apple', model='iPhone X', serial_number='1234567890',
            status='Available', checked_out_by=None, condition='Good')

    def test_device_str(self):
        self.assertEqual(
            str(self.device), 'Apple iPhone X (1234567890)')

    def test_device_checked_out_by_null(self):
        self.assertIsNone(self.device.checked_out_by)

    def test_device_checked_out_by_employee(self):
        self.device.checked_out_by = self.employee
        self.device.save()
        self.assertEqual(
            self.device.checked_out_by, self.employee)

# Device History Model Tests
class DeviceHistoryModelTests(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='abc company limt')
        self.employee = Employee.objects.create(
            company=self.company, name='Donal Tamp')
        self.device = Device.objects.create(
            company=self.company, make='Apple', model='iPhone X', serial_number='1234567890',
            status='Available', checked_out_by=None, condition='Good')

    def test_device_history_str(self):
        history = DeviceHistory(device=self.device, employee=self.employee)
        self.assertEqual(str(history), f"{self.device} - {self.employee}")

    def test_device_history_checked_out_date(self):
        history = DeviceHistory(device=self.device, employee=self.employee)
        history.save()
        self.assertIsNotNone(history.checked_out_date)

    def test_device_history_checked_in_date_null(self):
        history = DeviceHistory(device=self.device, employee=self.employee)
        history.save()
        self.assertIsNone(history.checked_in_date)

    def test_device_history_checked_in_date(self):
        history = DeviceHistory(device=self.device, employee=self.employee)
        history.save()
        history.checked_in_date = timezone.now()
        history.save()
        self.assertIsNotNone(history.checked_in_date)
