from django.db import models
from django.utils import timezone

# Create company models
class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
# Crate Employee models
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Crate Device models
class Device(models.Model):
    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Checked Out', 'Checked Out'),
        ('Maintenance', 'Maintenance')
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    status = models.CharField(
        max_length=255, choices=STATUS_CHOICES, default='Available')
    checked_out_by = models.ForeignKey(
        Employee, null=True, blank=True, on_delete=models.SET_NULL, related_name='checked_out_devices')
    condition = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.serial_number})"

#Crate device History model
class DeviceHistory(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out_date = models.DateTimeField(default=timezone.now)
    checked_in_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.device} - {self.employee}"
