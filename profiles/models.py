from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator, validate_email

# Create your models here.

class Profile(AbstractBaseUser):
    first_name = models.CharField(max_length = 120)
    last_name = models.CharField(max_length = 120)
    chinese_name = models.CharField(max_length = 6)
    gender = models.CharField(max_length = 10,choices = [('B','Brother'),('S','Sister')])
    locality = models.ForeignKey('Locality', on_delete = models.RESTRICT)
    district = models.CharField(max_length = 8)
    
    phone_regex = RegexValidator(regex=r'^[(]?[2-9]\d{2}[) -.]{0,2}\d{3}[ -.]?\d{4}$', message="Please enter your 10-digit phone number (including area code) without dashes or anything else.")
    phone_number = PhoneNumberField(validators = [phone_regex], max_length = 10) # validators should be a list

    email = models.CharField(validators = [validate_email], max_length = 255)
    usertypes = models.ManyToManyField('UserType')

    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey('self', on_delete = models.RESTRICT)