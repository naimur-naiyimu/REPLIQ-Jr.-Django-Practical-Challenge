from django.db import models
from app.models import Company

class PhoneCompany(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    phone_number = models.CharField(max_length=20)
    company = models.ForeignKey(PhoneCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone_number
