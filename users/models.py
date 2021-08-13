from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator, validate_email

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password = None):
        """
        Creates and saves a User with the given first name, last name, email, and password
        """

        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password = None):
        """
        Creates and saves a superuser with the given first and last name,        email, and password.
        """

        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password,
        )

        user.is_admin = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    first_name = models.CharField(max_length = 120)
    last_name = models.CharField(max_length = 120)
    chinese_name = models.CharField(max_length = 6)
    gender = models.CharField(max_length = 10,choices = [('B','Brother'),('S','Sister')])
    locality = models.ForeignKey('localities.Locality', on_delete = models.RESTRICT)
    district = models.CharField(max_length = 8)
    language = models.ForeignKey('languages.Language', verbose_name = 'Primary Language', on_delete = models.RESTRICT)
    
    phone_regex = RegexValidator(regex=r'^[(]?[2-9]\d{2}[) -.]{0,2}\d{3}[ -.]?\d{4}$', message="Please enter your 10-digit phone number (including area code) without dashes or anything else.")
    phone_number = PhoneNumberField(validators = [phone_regex], max_length = 10) # validators should be a list

    email = models.CharField(validators = [validate_email], max_length = 255)
    usertypes = models.ManyToManyField('userTypes.UserType')

    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()

    groups = models.ManyToManyField('Group')
    user_permissions = models.ManyToManyField('Permission')

    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey('self', on_delete = models.RESTRICT)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.first_name != '':
            return self.first_name+' '+self.last_name+' ('+self.locality+', '+self.district+')'
        else:
            return self.chinese_name+' ('+self.locality+', '+self.district+')'
    
    def has_perm(self, perm, obj = None):
        "Does the user have a specific permission?"
        #Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        #Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        #Simplest possible answer: All staff are staff
        return self.is_staff