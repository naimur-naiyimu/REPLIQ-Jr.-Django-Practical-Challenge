from django.contrib import admin
from .models import PhoneCompany, Subscriber

# Register your models here.
admin.site.register(PhoneCompany)
admin.site.register(Subscriber)