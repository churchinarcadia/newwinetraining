from django.conf import settings
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Term(models.Model):
    term = models.CharField(max_length = 10, choices = [('Fall'),('Spring')])
    year = models.IntegerField(
        validators = [
            MinValueValidator(2000, message='Please enter an appropriate year.'),
            MaxValueValidator(2040, message='Please enter an appropriate year.'),
        ],
    )
    language = models.ForeignKey('languages.Language', on_delete = models.RESTRICT)
    start_date = models.DateField(auto_now = False, auto_now_add = False)
    end_date = models.DateField(auto_now = False, auto_now_add = False, )
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)
    modified = models.DateTimeField(auto_now = True)
    modifier = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.RESTRICT)