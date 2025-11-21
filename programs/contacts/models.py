from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Contacts(models.Model):
    contact_firstname = models.CharField(max_length=50)
    contact_lastname=models.CharField(max_length=50)
    contact_email=models.EmailField(null=True, blank=True)
    contact_mobilenumber=PhoneNumberField(null=True, blank=True)
    contact_message=models.TextField()

