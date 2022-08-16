
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class CAR(models.Model):
    person = models.CharField(help_text = 'اسم صاحب السيارة '  , max_length=60, blank = True)
    C_number = models.IntegerField(unique = True)

    car_type_choices = (
    ('Private','Private'),
    ('Goverment', 'Goverment'),
    ('Taxi', 'Taxi'),
    )

    privGovTaxi = models.CharField(default='Private', help_text='اجرة - خصوصي - عمومي' , max_length=10 ,choices=car_type_choices)


    def __str__(self):
        self.C_number =str(self.C_number)
        return self.C_number



class VIOLATION(models.Model):
    desc=models.CharField(default="ركون خاطئ" , max_length=50)
    car = models.ForeignKey(CAR, related_name='violations', on_delete=models.CASCADE)
    V_number = models.BigAutoField(primary_key=True, editable=False)

    cost = models.PositiveIntegerField()
    created_dt = models.DateTimeField(auto_now_add=True)
    IsPaid = models.BooleanField(default=False)

    def __str__(self):
        o = self.V_number
        o =  str(self.cost)
        return str(self.cost) + " car number>" + str(self.car.C_number)

class CUSTOMER(models.Model):
    account = models.ForeignKey(User, auto_created=True,related_name='User', on_delete=models.CASCADE)
    test_number = models.IntegerField(unique = True, blank = True, null = True, default = None)
    car = models.ForeignKey(CAR, related_name='Car', on_delete=models.CASCADE)
    def __str__(self):
        return self.account.username


