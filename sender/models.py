from django.db import models

# USDISPATCH
CHOICES = (
    ('Dry_Van', 'Dry Van'),
    ('Reefer', 'Reefer'),
    ('Flatbed', 'Flatbed'),
    ('Box_Truck', 'Box Truck')
)
yes_no = (
    ('yes', 'Yes'),
    ('no', 'No'),
)

class Owner(models.Model):
    username = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.EmailField()
    dry_van = models.BooleanField(blank=True, null=True)
    reefer = models.BooleanField(blank=True, null=True)
    flatbed = models.BooleanField(blank=True, null=True)
    box_truck = models.BooleanField(blank=True, null=True)
    number_of_truck = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.email

class Career(models.Model):
    username = models.CharField(max_length=250)
    dba = models.CharField(max_length=250,blank=True, null=True)
    address = models.CharField(max_length=250,blank=True, null=True)
    apartment = models.CharField(max_length=250,blank=True, null=True)
    city = models.CharField(max_length=255,blank=True, null=True)
    state = models.CharField(max_length=255,blank=True, null=True)
    zip = models.CharField(max_length=250,blank=True, null=True)
    country = models.CharField(max_length=250,blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    usdot = models.CharField(max_length=250,blank=True, null=True)
    mc = models.CharField(max_length=250,blank=True, null=True)
    ssn = models.CharField(max_length=250,blank=True, null=True)
    number_of_drivers = models.CharField(max_length=250,blank=True, null=True)
    number_of_truck = models.CharField(max_length=250,blank=True, null=True)
    type_of_equipment = models.CharField(max_length=250, choices=CHOICES,blank=True, null=True)
    factor_invoices = models.CharField(max_length=250, choices=yes_no,blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    choice_file = models.FileField(upload_to='files', max_length=254,blank=True, null=True)

    def __str__(self):
        return self.email

class Freight_brokers(models.Model):
    username = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.EmailField()
    lane = models.CharField(max_length=250, blank=True, null=True)
    budget = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.email

class Contact(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.message

# USfuelsystems

class UsContact(models.Model):
    username = models.CharField(max_length=250, verbose_name='имя')
    phone = models.CharField(max_length=250, verbose_name='номер')