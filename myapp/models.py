from django.db import models

class Patients(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    passport = models.IntegerField(max_length=15)
    phone_number = models.IntegerField(max_length=15)
    email = models.CharField(max_length=50)
    ensurance_number = models.IntegerField(max_length=20)
    ensurance_type = models.CharField(max_length=20)
    ensurance_company = models.CharField(max_length=50)


class Company(models.Model):
    ensurance_company = models.CharField(max_length=50)
    ensurance_adress = models.CharField(max_length=255)
    ensurance_INN = models.IntegerField(max_length=20)
    ensurance_RS = models.IntegerField(max_length=20)
    ensurance_BIK = models.IntegerField(max_length=20)



class Orders(models.Model):
    order_date = models.DateField()
    services = models.CharField(max_length=255)
    order_status = models.CharField(max_length=50)
    order_service_status = models.CharField(max_length=50)
    order_complete_days = models.IntegerField(max_length=3)



class Services(models.Model):
    services = models.CharField(max_length=255)
    whom_gaven = models.CharField(max_length=255)
    analizator = models.CharField(max_length=255)



class Analizator(models.Model):
    analizator_date = models.DateField()
    analizator_time = models.TimeField()
    analizator_complete_date = models.DateField()
    analizator_complete_time = models.TimeField()



class Laborants(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    lasttime_enter = models.TimeField()
    lastdate_enter = models.DateField()
    services = models.CharField(max_length=255)




class Accountant(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    lasttime_enter = models.TimeField()
    lastdate_enter = models.DateField()
    services = models.CharField(max_length=255)
    checks = models.CharField(max_length=255)