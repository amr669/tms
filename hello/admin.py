from django.contrib import admin

# Register your models here.
from . models import CAR, CUSTOMER, VIOLATION
admin.site.register([CAR, CUSTOMER, VIOLATION])