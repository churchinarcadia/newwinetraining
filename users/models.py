from django.conf import settings
from django.db import models
from newwinetraining.models import BaseModel

from django.contrib.auth.models import Group, Permission

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator, validate_email

from django.utils.translation import gettext

from trainings.models import Term, Registration

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length = 100, verbose_name = gettext('Name'))
    description = models.CharField(max_length = 255, verbose_name = gettext('Description'))
    active = models.BooleanField(default = True, verbose_name = gettext('Active'))
    created = models.DateTimeField(auto_now_add = True, verbose_name = gettext('Created'))
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'usertype_creators', verbose_name = gettext('Creator'), on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True, verbose_name = gettext('Modified'))
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'usertype_modifiers', verbose_name = gettext('Modifier'), on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.name

class Locality(models.Model):
    locality = models.CharField(max_length = 100, verbose_name = gettext('Locality'))
    active = models.BooleanField(default = True, verbose_name = gettext('Active'))
    created = models.DateTimeField(auto_now_add = True, verbose_name = gettext('Created'))
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'locality_creators', verbose_name = gettext('Creator'), on_delete = models.RESTRICT, blank = True, null = True)
    modified = models.DateTimeField(auto_now = True, verbose_name = gettext('Modified'))
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'locality_modifiers', verbose_name = gettext('Modifier'), on_delete = models.RESTRICT, blank = True, null = True)

    def __str__(self):
        return self.locality

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password = None):
        """
        Creates and saves a User with the given first name, last name, email, and password
        """

        if not email:
            raise ValueError(gettext('Users must have an email address.'))

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
        Creates and saves a superuser with the given first and last name, email, and password.
        """

        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    first_name = models.CharField(max_length = 120, blank = True, verbose_name = gettext('First Name'))
    last_name = models.CharField(max_length = 120, blank = True, verbose_name = gettext('Last Name'))
    chinese_name = models.CharField(max_length = 6, blank = True, verbose_name = gettext('Chinese Name'))
    gender = models.CharField(max_length = 10, choices = [('B',gettext('Brother')),('S',gettext('Sister'))], verbose_name = gettext('Gender'), blank = True, null = True)
    locality = models.ForeignKey(Locality, related_name = 'user_localities', verbose_name = gettext('Locality'), on_delete = models.RESTRICT, blank = True, null = True)
    district = models.CharField(max_length = 8, verbose_name = gettext('District'), blank = True, null = True)
    language = models.ForeignKey('languages.Language', related_name = 'user_languages', verbose_name = gettext('Primary Language'), on_delete = models.RESTRICT, blank = True, null = True)
    
    #phone_regex = RegexValidator(regex=r'^[(]?[2-9]\d{2}[) -.]{0,2}\d{3}[ -.]?\d{4}$', message="Please enter your 10-digit phone number including your area code.")
    #phone_number = PhoneNumberField(validators = [phone_regex], max_length = 12, blank = True, null = True) # validators should be a list
    phone_number = PhoneNumberField(max_length = 12, verbose_name = gettext('Phone Number'), blank = True, null = True)

    email = models.CharField(validators = [validate_email], max_length = 255, verbose_name = gettext('Email'), unique = True)
    usertypes = models.ManyToManyField(UserType, related_name = 'user_usertypes', verbose_name = gettext('User Types'), blank = True)

    is_staff = models.BooleanField(default = False, verbose_name = gettext('Is Staff'))
    is_superuser = models.BooleanField(default = False, verbose_name = gettext('Is Superuser'))
    last_login = models.DateTimeField(verbose_name = gettext('Last Login'), blank = True, null = True)

    groups = models.ManyToManyField(Group, related_name = 'user_groups', verbose_name = gettext('Groups'), blank = True)
    user_permissions = models.ManyToManyField(Permission, related_name = 'user_userpermissions', verbose_name = gettext('User-specific Permissions'), blank = True)

    created = models.DateTimeField(auto_now_add = True, verbose_name = gettext('Created'), null = True)
    modified = models.DateTimeField(auto_now = True, verbose_name = gettext('Modified'), null = True)
    modifier = models.ForeignKey('self', related_name = 'user_modifiers', verbose_name = gettext('Modifier'), on_delete = models.RESTRICT, blank = True, null = True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
#        return self.first_name + ' ' + self.last_name
        if self.locality:
            locality = ' (' + str(self.locality) + ', ' + self.district +')'
        else:
            locality = ''
            
        if self.first_name != '':
            return self.first_name + ' ' + self.last_name + locality
        else:
            return self.chinese_name + locality
        
    
    def has_perm(self, perm, obj = None):
        "Does the user have a specific permission?"
        #Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        #Simplest possible answer: Yes, always
        return True
    
    @property
    def has_staff_perms(self):
        "Is the user a member of staff?"
        #Simplest possible answer: All staff are staff
        return self.is_staff

    @property
    def has_superuser_perms(self):
        "Is the user a member of superusers?"
        #Simplest possible answer: All staff are staff
        return self.is_superuser
    
    def get_short_name(self):
        if self.first_name != '':
            return self.first_name
        else:
            return self.chinese_name
    
    def get_full_name(self):
        if self.first_name != '':
            return self.first_name + ' ' + self.last_name
        else:
            return self.chinese_name
    
    def has_role(self, target):
        
        roles = list(self.groups.values_list('name', flat = True))
        
        registered_this_term = self.registration_users.filter(pk = Term.objects.current_terms())
        registered_last_term = self.registration_users.filter(pk = Term.objects.last_terms())
        
        if (Term.objects.current_terms.exists() and not registered_this_term.exists()) or (not Term.objects.current_term.exists() and not registered_last_term.exists()):
            if 'Trainee' in roles:
                roles.remove('Trainee')
        
        if self.has_staff_perms:
            roles += 'Staff'
        
        if self.has_superuser_perms:
            roles += 'Superuser'
            
        if target == '' or len(target.intersection(roles)) > 0:
            return True
        else:
            return False
    
    def registered_this_term(self):
        registered_this_term = self.registration_users.filter(pk = Term.objects.current_terms())
        
        if registered_this_term.exists():
            return True
        else:
            return False
    
    def registered_last_term(self):
        registered_last_term = self.registration_users.filter(pk = Term.objects.last_terms())
        
        if registered_last_term.exists():
            return True
        else:
            return False